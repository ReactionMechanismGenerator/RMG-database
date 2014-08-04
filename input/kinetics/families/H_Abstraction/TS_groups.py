#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/TS_groups"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "X_H_or_Xrad_H_Xbirad_H_Xtrirad_H",
    group = "OR{X_H, Xrad_H, Xbirad_H, Xtrirad_H}",
    distances = DistanceData(
        distances = {'d12': 1.331716, 'd13': 2.659403, 'd23': 1.332364},
        uncertainties = {'d12': 0.080268, 'd13': 0.066794, 'd23': 0.078274},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1648 distances.
[<Entry index=44 label="CO/H/NonDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=73 label="C/H3/O">, <Entry index=170 label="H_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=37 label="Cd/H/Ct">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=176 label="O_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=212 label="Cb_rad">]
[<Entry index=145 label="C/H/CdCd">, <Entry index=232 label="C_methyl">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=181 label="OOCH3">]
[<Entry index=42 label="CO_pri">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=168 label="CH2_triplet">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=212 label="Cb_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=172 label="O2b">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=42 label="CO_pri">, <Entry index=172 label="O2b">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=45 label="InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3">, <Entry index=232 label="C_methyl">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=181 label="OOCH3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=4 label="H2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=172 label="O2b">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=170 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/CO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=119 label="C/H/Cs2O">, <Entry index=170 label="H_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=73 label="C/H3/O">, <Entry index=181 label="OOCH3">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=73 label="C/H3/O">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=11 label="H2O2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=4 label="H2">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=172 label="O2b">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=212 label="Cb_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=212 label="Cb_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=172 label="O2b">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=212 label="Cb_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=168 label="CH2_triplet">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=232 label="C_methyl">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=181 label="OOCH3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=168 label="CH2_triplet">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=296 label="C_rad/Cs2O">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=181 label="OOCH3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=181 label="OOCH3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=170 label="H_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=7 label="O_pri">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=60 label="C_methane">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=40 label="Cb_H">, <Entry index=181 label="OOCH3">]
[<Entry index=13 label="ROOH_sec">, <Entry index=172 label="O2b">]
[<Entry index=73 label="C/H3/O">, <Entry index=168 label="CH2_triplet">]
[<Entry index=12 label="ROOH_pri">, <Entry index=212 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=203 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=181 label="OOCH3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=73 label="C/H3/O">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=232 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=11 label="H2O2">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=168 label="CH2_triplet">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=45 label="InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=14 label="ROOH_ter">, <Entry index=232 label="C_methyl">]
[<Entry index=60 label="C_methane">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=42 label="CO_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=60 label="C_methane">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=12 label="ROOH_pri">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=60 label="C_methane">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=7 label="O_pri">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=181 label="OOCH3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=232 label="C_methyl">]
[<Entry index=73 label="C/H3/O">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=11 label="H2O2">, <Entry index=181 label="OOCH3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=60 label="C_methane">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=42 label="CO_pri">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=16 label="Orad_O_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=181 label="OOCH3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=172 label="O2b">]
[<Entry index=4 label="H2">, <Entry index=239 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=172 label="O2b">]
[<Entry index=11 label="H2O2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=7 label="O_pri">, <Entry index=170 label="H_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=168 label="CH2_triplet">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=7 label="O_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/CO">, <Entry index=232 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=232 label="C_methyl">]
[<Entry index=72 label="C/H3/CO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=73 label="C/H3/O">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=7 label="O_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=170 label="H_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=168 label="CH2_triplet">]
[<Entry index=60 label="C_methane">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=181 label="OOCH3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=454 label="O/H/OneDeC">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=7 label="O_pri">, <Entry index=212 label="Cb_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=60 label="C_methane">, <Entry index=176 label="O_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=170 label="H_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=443 label="OH_rad_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=60 label="C_methane">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=232 label="C_methyl">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=232 label="C_methyl">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=40 label="Cb_H">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=443 label="OH_rad_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=181 label="OOCH3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=170 label="H_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=172 label="O2b">]
[<Entry index=37 label="Cd/H/Ct">, <Entry index=170 label="H_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=232 label="C_methyl">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=42 label="CO_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=60 label="C_methane">, <Entry index=321 label="C_rad/CdCdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=176 label="O_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=42 label="CO_pri">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=271 label="C_rad/H/OneDeO">]
[<Entry index=60 label="C_methane">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=73 label="C/H3/O">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=212 label="Cb_rad">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=212 label="Cb_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=176 label="O_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=168 label="CH2_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=40 label="Cb_H">, <Entry index=170 label="H_rad">]
[<Entry index=7 label="O_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=212 label="Cb_rad">]
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=212 label="Cb_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=7 label="O_pri">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=170 label="H_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=176 label="O_pri_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=60 label="C_methane">, <Entry index=181 label="OOCH3">]
[<Entry index=60 label="C_methane">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=170 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=60 label="C_methane">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=443 label="OH_rad_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=60 label="C_methane">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=232 label="C_methyl">]
[<Entry index=16 label="Orad_O_H">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=73 label="C/H3/O">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=181 label="OOCH3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=42 label="CO_pri">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=73 label="C/H3/O">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=443 label="OH_rad_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=170 label="H_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/CO">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=60 label="C_methane">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=176 label="O_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=73 label="C/H3/O">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=60 label="C_methane">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=232 label="C_methyl">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=182 label="O_rad/OneDe">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=181 label="OOCH3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=176 label="O_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=7 label="O_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=443 label="OH_rad_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=212 label="Cb_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=181 label="OOCH3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=232 label="C_methyl">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=168 label="CH2_triplet">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=4 label="H2">, <Entry index=168 label="CH2_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=170 label="H_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=4 label="H2">, <Entry index=236 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=4 label="H2">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=172 label="O2b">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=40 label="Cb_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=72 label="C/H3/CO">, <Entry index=168 label="CH2_triplet">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=443 label="OH_rad_H">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=270 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=72 label="C/H3/CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=16 label="Orad_O_H">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=73 label="C/H3/O">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=168 label="CH2_triplet">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=212 label="Cb_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=170 label="H_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=11 label="H2O2">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=81 label="C/H2/O2">, <Entry index=232 label="C_methyl">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=212 label="Cb_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=172 label="O2b">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=172 label="O2b">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=42 label="CO_pri">, <Entry index=168 label="CH2_triplet">]
[<Entry index=16 label="Orad_O_H">, <Entry index=181 label="OOCH3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=42 label="CO_pri">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=212 label="Cb_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=232 label="C_methyl">]
[<Entry index=12 label="ROOH_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=209 label="Cd_rad/Ct">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/CO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=168 label="CH2_triplet">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=181 label="OOCH3">]
[<Entry index=73 label="C/H3/O">, <Entry index=172 label="O2b">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=170 label="H_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=209 label="Cd_rad/Ct">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=60 label="C_methane">, <Entry index=212 label="Cb_rad">]
[<Entry index=11 label="H2O2">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=212 label="Cb_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=42 label="CO_pri">, <Entry index=181 label="OOCH3">]
[<Entry index=73 label="C/H3/O">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=73 label="C/H3/O">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=232 label="C_methyl">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=232 label="C_methyl">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=232 label="C_methyl">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=170 label="H_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/CO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=232 label="C_methyl">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=4 label="H2">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=72 label="C/H3/CO">, <Entry index=170 label="H_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=181 label="OOCH3">]
[<Entry index=93 label="C/H2/OneDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=60 label="C_methane">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=176 label="O_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=60 label="C_methane">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=181 label="OOCH3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=60 label="C_methane">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=42 label="CO_pri">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=214 label="CO_pri_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 2,
    label = "Y_rad_birad_trirad_quadrad",
    group = "OR{Y_2centeradjbirad, Y_1centerbirad, Y_rad, Y_1centertrirad, Y_1centerquadrad}",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 3,
    label = "X_H",
    group = 
"""
1 *1 R 0 {2,S}
2 *2 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.002606, 'd13': 0.000452, 'd23': 0.003146},
        uncertainties = {'d12': 0.079902, 'd13': 0.066625, 'd23': 0.078448},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1601 distances.
[<Entry index=44 label="CO/H/NonDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=73 label="C/H3/O">, <Entry index=170 label="H_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=37 label="Cd/H/Ct">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=176 label="O_pri_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=212 label="Cb_rad">]
[<Entry index=145 label="C/H/CdCd">, <Entry index=232 label="C_methyl">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=181 label="OOCH3">]
[<Entry index=42 label="CO_pri">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=168 label="CH2_triplet">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=212 label="Cb_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=172 label="O2b">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=42 label="CO_pri">, <Entry index=172 label="O2b">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=45 label="InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3">, <Entry index=232 label="C_methyl">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=181 label="OOCH3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=4 label="H2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=172 label="O2b">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=170 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/CO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=119 label="C/H/Cs2O">, <Entry index=170 label="H_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=73 label="C/H3/O">, <Entry index=181 label="OOCH3">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=73 label="C/H3/O">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=11 label="H2O2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=4 label="H2">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=172 label="O2b">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=212 label="Cb_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=212 label="Cb_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=172 label="O2b">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=212 label="Cb_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=168 label="CH2_triplet">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=232 label="C_methyl">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=181 label="OOCH3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=168 label="CH2_triplet">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=296 label="C_rad/Cs2O">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=181 label="OOCH3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=181 label="OOCH3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=170 label="H_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=7 label="O_pri">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=60 label="C_methane">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=40 label="Cb_H">, <Entry index=181 label="OOCH3">]
[<Entry index=13 label="ROOH_sec">, <Entry index=172 label="O2b">]
[<Entry index=73 label="C/H3/O">, <Entry index=168 label="CH2_triplet">]
[<Entry index=12 label="ROOH_pri">, <Entry index=212 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=203 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=181 label="OOCH3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=73 label="C/H3/O">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=232 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=11 label="H2O2">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=168 label="CH2_triplet">]
[<Entry index=72 label="C/H3/CO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=45 label="InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=14 label="ROOH_ter">, <Entry index=232 label="C_methyl">]
[<Entry index=60 label="C_methane">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=42 label="CO_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=60 label="C_methane">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=12 label="ROOH_pri">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=60 label="C_methane">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=7 label="O_pri">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=181 label="OOCH3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=232 label="C_methyl">]
[<Entry index=73 label="C/H3/O">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=11 label="H2O2">, <Entry index=181 label="OOCH3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=60 label="C_methane">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=42 label="CO_pri">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=16 label="Orad_O_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=181 label="OOCH3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=172 label="O2b">]
[<Entry index=4 label="H2">, <Entry index=239 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=172 label="O2b">]
[<Entry index=11 label="H2O2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=7 label="O_pri">, <Entry index=170 label="H_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=168 label="CH2_triplet">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=7 label="O_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/CO">, <Entry index=232 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=4 label="H2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=232 label="C_methyl">]
[<Entry index=72 label="C/H3/CO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=73 label="C/H3/O">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=7 label="O_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=170 label="H_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=168 label="CH2_triplet">]
[<Entry index=60 label="C_methane">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=181 label="OOCH3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=454 label="O/H/OneDeC">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=7 label="O_pri">, <Entry index=212 label="Cb_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=60 label="C_methane">, <Entry index=176 label="O_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=170 label="H_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=42 label="CO_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=60 label="C_methane">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=232 label="C_methyl">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=232 label="C_methyl">]
[<Entry index=40 label="Cb_H">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=181 label="OOCH3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=170 label="H_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=172 label="O2b">]
[<Entry index=37 label="Cd/H/Ct">, <Entry index=170 label="H_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=232 label="C_methyl">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=42 label="CO_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=60 label="C_methane">, <Entry index=321 label="C_rad/CdCdCs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=176 label="O_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=42 label="CO_pri">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=271 label="C_rad/H/OneDeO">]
[<Entry index=60 label="C_methane">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=73 label="C/H3/O">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=212 label="Cb_rad">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=212 label="Cb_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=176 label="O_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=168 label="CH2_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=40 label="Cb_H">, <Entry index=170 label="H_rad">]
[<Entry index=7 label="O_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=212 label="Cb_rad">]
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=212 label="Cb_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=7 label="O_pri">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=170 label="H_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=176 label="O_pri_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=60 label="C_methane">, <Entry index=181 label="OOCH3">]
[<Entry index=60 label="C_methane">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=170 label="H_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=60 label="C_methane">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=60 label="C_methane">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=232 label="C_methyl">]
[<Entry index=16 label="Orad_O_H">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=73 label="C/H3/O">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=181 label="OOCH3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=42 label="CO_pri">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=181 label="OOCH3">]
[<Entry index=73 label="C/H3/O">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=170 label="H_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/CO">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=60 label="C_methane">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=176 label="O_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=73 label="C/H3/O">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=60 label="C_methane">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=232 label="C_methyl">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=182 label="O_rad/OneDe">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=176 label="O_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=7 label="O_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=73 label="C/H3/O">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=212 label="Cb_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=181 label="OOCH3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=232 label="C_methyl">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=168 label="CH2_triplet">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=4 label="H2">, <Entry index=168 label="CH2_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=170 label="H_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=4 label="H2">, <Entry index=236 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=4 label="H2">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=172 label="O2b">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=40 label="Cb_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=72 label="C/H3/CO">, <Entry index=168 label="CH2_triplet">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=270 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=72 label="C/H3/CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=16 label="Orad_O_H">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=73 label="C/H3/O">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=168 label="CH2_triplet">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=212 label="Cb_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=170 label="H_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=11 label="H2O2">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=81 label="C/H2/O2">, <Entry index=232 label="C_methyl">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=212 label="Cb_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=172 label="O2b">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=172 label="O2b">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=42 label="CO_pri">, <Entry index=168 label="CH2_triplet">]
[<Entry index=16 label="Orad_O_H">, <Entry index=181 label="OOCH3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=42 label="CO_pri">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=212 label="Cb_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=232 label="C_methyl">]
[<Entry index=12 label="ROOH_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=209 label="Cd_rad/Ct">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/CO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=168 label="CH2_triplet">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=181 label="OOCH3">]
[<Entry index=73 label="C/H3/O">, <Entry index=172 label="O2b">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=209 label="Cd_rad/Ct">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=60 label="C_methane">, <Entry index=212 label="Cb_rad">]
[<Entry index=11 label="H2O2">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=212 label="Cb_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=42 label="CO_pri">, <Entry index=181 label="OOCH3">]
[<Entry index=73 label="C/H3/O">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=73 label="C/H3/O">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=232 label="C_methyl">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=232 label="C_methyl">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=232 label="C_methyl">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=170 label="H_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/CO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=232 label="C_methyl">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=4 label="H2">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=72 label="C/H3/CO">, <Entry index=170 label="H_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=181 label="OOCH3">]
[<Entry index=93 label="C/H2/OneDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=60 label="C_methane">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=176 label="O_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=60 label="C_methane">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=181 label="OOCH3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=60 label="C_methane">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=42 label="CO_pri">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=214 label="CO_pri_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 4,
    label = "H2",
    group = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.330672, 'd13': -0.369719, 'd23': -0.04202},
        uncertainties = {'d12': 0.180791, 'd13': 0.152945, 'd23': 0.111491},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 64 distances.
[<Entry index=4 label="H2">, <Entry index=203 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=4 label="H2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=4 label="H2">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=168 label="CH2_triplet">]
[<Entry index=4 label="H2">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=4 label="H2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=239 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=4 label="H2">, <Entry index=236 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=4 label="H2">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=209 label="Cd_rad/Ct">]
[<Entry index=4 label="H2">, <Entry index=296 label="C_rad/Cs2O">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=4 label="H2">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=4 label="H2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=182 label="O_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=181 label="OOCH3">]
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=4 label="H2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=4 label="H2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=4 label="H2">, <Entry index=176 label="O_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=212 label="Cb_rad">]
[<Entry index=4 label="H2">, <Entry index=293 label="C_rad/Cs3">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 409,
    label = "N3_H",
    group = 
"""
1 *1 {N3s,N3d} 0 {2,S}
2 *2 H         0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 413,
    label = "N3d_H",
    group = 
"""
1 *1 N3d 0 {2,S} {3,D}
2 *2 H   0 {1,S}
3    R!H 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 465,
    label = "N3d/H/NonDe",
    group = 
"""
1 *1 N3d      0 {2,S} {3,D}
2 *2 H        0 {1,S}
3    {N3d,Od} 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 447,
    label = "N3d/H/NonDeO",
    group = 
"""
1 *1 N3d 0 {2,S} {3,D}
2 *2 H   0 {1,S}
3    O   0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 448,
    label = "N3d/H/NonDeN",
    group = 
"""
1 *1 N3d 0 {2,S} {3,D}
2 *2 H   0 {1,S}
3    N3d 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 446,
    label = "N3d/H/NonDeC",
    group = 
"""
1 *1 N3d 0 {2,S} {3,D}
2 *2 H   0 {1,S}
3    Cd  0 {1,D} {4,S} {5,S}
4    R   0 {3,S}
5    R   0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 466,
    label = "N3d/H/OneDe",
    group = 
"""
1 *1 N3d                0 {2,S} {3,D}
2 *2 H                  0 {1,S}
3    {Cd,Ct,Cb,N5d,N5t} 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 467,
    label = "N3d/H/OneDeC",
    group = 
"""
1 *1 N3d        0 {2,S} {3,D}
2 *2 H          0 {1,S}
3    {Cd,Ct,Cb} 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 468,
    label = "N3d/H/OneDeN",
    group = 
"""
1 *1 N3d       0 {2,S} {3,D}
2 *2 H         0 {1,S}
3    {N5d,N5t} 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 402,
    label = "N3s_H",
    group = 
"""
1 *1 N3s 0 {2,S} {3,S} {4,S}
2 *2 H   0 {1,S}
3    R   0 {1,S}
4    R   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 410,
    label = "NH3",
    group = 
"""
1 *1 N3s 0 {2,S} {3,S} {4,S}
2 *2 H   0 {1,S}
3    H   0 {1,S}
4    H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 411,
    label = "N3s_pri_H",
    group = 
"""
1 *1 N3s 0 {2,S} {3,S} {4,S}
2 *2 H   0 {1,S}
3    H   0 {1,S}
4    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 450,
    label = "N3s/H2/NonDe",
    group = 
"""
1 *1 N3s         0 {2,S} {3,S} {4,S}
2 *2 H           0 {1,S}
3    H           0 {1,S}
4    {N3s,Cs,Os} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 451,
    label = "N3s/H2/NonDeC",
    group = 
"""
1 *1 N3s 0 {2,S} {3,S} {4,S}
2 *2 H   0 {1,S}
3    H   0 {1,S}
4    Cs  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 452,
    label = "N3s/H2/NonDeO",
    group = 
"""
1 *1 N3s 0 {2,S} {3,S} {4,S}
2 *2 H   0 {1,S}
3    H   0 {1,S}
4    Os  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 453,
    label = "N3s/H2/NonDeN",
    group = 
"""
1 *1 N3s 0 {2,S} {3,S} {4,S}
2 *2 H   0 {1,S}
3    H   0 {1,S}
4    N3s 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 472,
    label = "N3s/H2/OneDe",
    group = 
"""
1 *1 N3s       0 {2,S} {3,S} {4,S}
2 *2 H         0 {1,S}
3    H         0 {1,S}
4    {N3d,N5d} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 473,
    label = "N3s/H2/OneDeN",
    group = 
"""
1 *1 N3s       0 {2,S} {3,S} {4,S}
2 *2 H         0 {1,S}
3    H         0 {1,S}
4    {N3d,N5d} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 412,
    label = "N3s_sec_H",
    group = 
"""
1 *1 N3s 0 {2,S} {3,S} {4,S}
2 *2 H   0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 414,
    label = "N5_H",
    group = 
"""
1 *1 {N5s,N5d,N5dd,N5t,N5b} 0 {2,S}
2 *2 H                      0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 415,
    label = "N5d_H",
    group = 
"""
1 *1 N5d 0 {2,S}
2 *2 H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 456,
    label = "N5d/H/NonDeOO",
    group = 
"""
1 *1 N5d 0 {2,S} {3,S} {4,D}
2 *2 H   0 {1,S}
3    Os  0 {1,S}
4    Od  0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 5,
    label = "Ct_H",
    group = 
"""
1 *1 Ct    0 {2,T} {3,S}
2    {C,N} 0 {1,T}
3 *2 H     0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.408669, 'd13': 0.157512, 'd23': -0.195879},
        uncertainties = {'d12': 0.304899, 'd13': 0.29804, 'd23': 0.228569},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 6 distances.
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=212 label="Cb_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 457,
    label = "Ct/H/NonDeC",
    group = 
"""
1 *1 Ct 0 {2,S} {3,T}
2 *2 H  0 {1,S}
3    Ct 0 {1,T}
""",
    distances = DistanceData(
        distances = {'d12': 0.408669, 'd13': 0.157512, 'd23': -0.195879},
        uncertainties = {'d12': 0.304899, 'd13': 0.29804, 'd23': 0.228569},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 6 distances.
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=212 label="Cb_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 458,
    label = "Ct/H/NonDeN",
    group = 
"""
1 *1 Ct  0 {2,S} {3,T}
2 *2 H   0 {1,S}
3    N3t 0 {1,T}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 6,
    label = "O_H",
    group = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    R 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.094821, 'd13': -0.144102, 'd23': -0.044386},
        uncertainties = {'d12': 0.106621, 'd13': 0.082075, 'd23': 0.102029},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 171 distances.
[<Entry index=9 label="O/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=181 label="OOCH3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=181 label="OOCH3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=11 label="H2O2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=172 label="O2b">]
[<Entry index=11 label="H2O2">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=7 label="O_pri">, <Entry index=170 label="H_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=7 label="O_pri">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=12 label="ROOH_pri">, <Entry index=181 label="OOCH3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=172 label="O2b">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=11 label="H2O2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=11 label="H2O2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=11 label="H2O2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=11 label="H2O2">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=11 label="H2O2">, <Entry index=212 label="Cb_rad">]
[<Entry index=7 label="O_pri">, <Entry index=212 label="Cb_rad">]
[<Entry index=11 label="H2O2">, <Entry index=232 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=7 label="O_pri">, <Entry index=232 label="C_methyl">]
[<Entry index=7 label="O_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=11 label="H2O2">, <Entry index=176 label="O_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=168 label="CH2_triplet">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=232 label="C_methyl">]
[<Entry index=12 label="ROOH_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=11 label="H2O2">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=13 label="ROOH_sec">, <Entry index=172 label="O2b">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=212 label="Cb_rad">]
[<Entry index=7 label="O_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=11 label="H2O2">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=170 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=168 label="CH2_triplet">]
[<Entry index=7 label="O_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=14 label="ROOH_ter">, <Entry index=232 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=181 label="OOCH3">]
[<Entry index=7 label="O_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=454 label="O/H/OneDeC">, <Entry index=170 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=214 label="CO_pri_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 7,
    label = "O_pri",
    group = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.094431, 'd13': -0.134837, 'd23': -0.198702},
        uncertainties = {'d12': 0.176008, 'd13': 0.157532, 'd23': 0.063686},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 13 distances.
[<Entry index=7 label="O_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=7 label="O_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=212 label="Cb_rad">]
[<Entry index=7 label="O_pri">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=7 label="O_pri">, <Entry index=232 label="C_methyl">]
[<Entry index=7 label="O_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=7 label="O_pri">, <Entry index=170 label="H_rad">]
[<Entry index=7 label="O_pri">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=7 label="O_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=7 label="O_pri">, <Entry index=180 label="O_rad/NonDeO">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 8,
    label = "O_sec",
    group = 
"""
1 *1 O   0 {2,S} {3,S}
2 *2 H   0 {1,S}
3    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.109396, 'd13': -0.144816, 'd23': -0.032501},
        uncertainties = {'d12': 0.101872, 'd13': 0.075789, 'd23': 0.105027},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 158 distances.
[<Entry index=9 label="O/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=181 label="OOCH3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=181 label="OOCH3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=11 label="H2O2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=172 label="O2b">]
[<Entry index=11 label="H2O2">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=12 label="ROOH_pri">, <Entry index=181 label="OOCH3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=172 label="O2b">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=11 label="H2O2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=11 label="H2O2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=11 label="H2O2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=11 label="H2O2">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=11 label="H2O2">, <Entry index=212 label="Cb_rad">]
[<Entry index=11 label="H2O2">, <Entry index=232 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=11 label="H2O2">, <Entry index=176 label="O_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=168 label="CH2_triplet">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=232 label="C_methyl">]
[<Entry index=12 label="ROOH_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=11 label="H2O2">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=13 label="ROOH_sec">, <Entry index=172 label="O2b">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=212 label="Cb_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=11 label="H2O2">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=170 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=168 label="CH2_triplet">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=14 label="ROOH_ter">, <Entry index=232 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=181 label="OOCH3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=454 label="O/H/OneDeC">, <Entry index=170 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=214 label="CO_pri_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 9,
    label = "O/H/NonDeC",
    group = 
"""
1 *1 O  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.051922, 'd13': -0.154037, 'd23': -0.097214},
        uncertainties = {'d12': 0.075774, 'd13': 0.071514, 'd23': 0.049852},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 44 distances.
[<Entry index=9 label="O/H/NonDeC">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=168 label="CH2_triplet">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=181 label="OOCH3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 10,
    label = "O/H/NonDeO",
    group = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    O 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.130261, 'd13': -0.140197, 'd23': -0.007763},
        uncertainties = {'d12': 0.11173, 'd13': 0.06367, 'd23': 0.113634},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 113 distances.
[<Entry index=11 label="H2O2">, <Entry index=168 label="CH2_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=181 label="OOCH3">]
[<Entry index=11 label="H2O2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=232 label="C_methyl">]
[<Entry index=12 label="ROOH_pri">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=11 label="H2O2">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=181 label="OOCH3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=172 label="O2b">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=232 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=176 label="O_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=170 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=170 label="H_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=11 label="H2O2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=172 label="O2b">]
[<Entry index=11 label="H2O2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=11 label="H2O2">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=14 label="ROOH_ter">, <Entry index=232 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=11 label="H2O2">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=11 label="H2O2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=181 label="OOCH3">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=11 label="H2O2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=212 label="Cb_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=13 label="ROOH_sec">, <Entry index=172 label="O2b">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=212 label="Cb_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=214 label="CO_pri_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 11,
    label = "H2O2",
    group = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S} {4,S}
3 *2 H 0 {1,S}
4    H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.164599, 'd13': -0.140006, 'd23': 0.026735},
        uncertainties = {'d12': 0.075341, 'd13': 0.066433, 'd23': 0.118382},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 31 distances.
[<Entry index=11 label="H2O2">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=11 label="H2O2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=181 label="OOCH3">]
[<Entry index=11 label="H2O2">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=176 label="O_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=11 label="H2O2">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=11 label="H2O2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=168 label="CH2_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=11 label="H2O2">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=11 label="H2O2">, <Entry index=212 label="Cb_rad">]
[<Entry index=11 label="H2O2">, <Entry index=232 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=214 label="CO_pri_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 12,
    label = "ROOH_pri",
    group = 
"""
1 *1 O  0 {2,S} {7,S}
2    O  0 {1,S} {3,S}
3    C  0 {2,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
7 *2 H  0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.150544, 'd13': -0.13338, 'd23': 0.019329},
        uncertainties = {'d12': 0.045634, 'd13': 0.055505, 'd23': 0.079875},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 24 distances.
[<Entry index=12 label="ROOH_pri">, <Entry index=172 label="O2b">]
[<Entry index=12 label="ROOH_pri">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=212 label="Cb_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=181 label="OOCH3">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 13,
    label = "ROOH_sec",
    group = 
"""
1 *1 O  0 {2,S} {7,S}
2    O  0 {1,S} {3,S}
3    C  0 {2,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    H  0 {3,S}
7 *2 H  0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.025953, 'd13': -0.172756, 'd23': -0.142701},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=13 label="ROOH_sec">, <Entry index=172 label="O2b">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 14,
    label = "ROOH_ter",
    group = 
"""
1 *1 O  0 {2,S} {7,S}
2    O  0 {1,S} {3,S}
3    C  0 {2,S} {4,S} {5,S} {6,S}
4    Cs 0 {3,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
7 *2 H  0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.20991, 'd13': -0.111159, 'd23': 0.096061},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=14 label="ROOH_ter">, <Entry index=232 label="C_methyl">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 471,
    label = "O/H/NonDeN",
    group = 
"""
1 *1 O   0 {2,S} {3,S}
2 *2 H   0 {1,S}
3    N3s 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 15,
    label = "O/H/OneDe",
    group = 
"""
1 *1 O                        0 {2,S} {3,S}
2 *2 H                        0 {1,S}
3    {Cd,Ct,Cb,CO,CS,N3d,N5d} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.238232, 'd13': -0.375457, 'd23': -0.133531},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=454 label="O/H/OneDeC">, <Entry index=170 label="H_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 454,
    label = "O/H/OneDeC",
    group = 
"""
1 *1 O                0 {2,S} {3,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.238232, 'd13': -0.375457, 'd23': -0.133531},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=454 label="O/H/OneDeC">, <Entry index=170 label="H_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 455,
    label = "O/H/OneDeN",
    group = 
"""
1 *1 O         0 {2,S} {3,S}
2 *2 H         0 {1,S}
3    {N3d,N5d} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 16,
    label = "Orad_O_H",
    group = 
"""
1 *1 O 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    O 1 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.246232, 'd13': -0.050436, 'd23': 0.198742},
        uncertainties = {'d12': 0.065774, 'd13': 0.128293, 'd23': 0.174175},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 18 distances.
[<Entry index=16 label="Orad_O_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=181 label="OOCH3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=16 label="Orad_O_H">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=265 label="C_rad/H/CdCs">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 17,
    label = "S_H",
    group = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    R 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 18,
    label = "S_pri",
    group = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 19,
    label = "S_sec",
    group = 
"""
1 *1 S   0 {2,S} {3,S}
2 *2 H   0 {1,S}
3    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 20,
    label = "S/H/NonDeC",
    group = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 21,
    label = "S/H/NonDeS",
    group = 
"""
1 *1 S 0 {2,S} {3,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 22,
    label = "S/H/OneDe",
    group = 
"""
1 *1 S                0 {2,S} {3,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 23,
    label = "S/H/Cd",
    group = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 24,
    label = "S/H/CS",
    group = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S} {4,D}
4    S  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 25,
    label = "S/H/Ct",
    group = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 26,
    label = "S/H/Cb",
    group = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 27,
    label = "S/H/CO",
    group = 
"""
1 *1 S  0 {2,S} {3,S}
2 *2 H  0 {1,S}
3    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 28,
    label = "Cd_H",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    R 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.085916, 'd13': 0.013064, 'd23': -0.073486},
        uncertainties = {'d12': 0.132036, 'd13': 0.085886, 'd23': 0.108785},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 148 distances.
[<Entry index=35 label="Cd/H/Cd">, <Entry index=232 label="C_methyl">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=170 label="H_rad">]
[<Entry index=37 label="Cd/H/Ct">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=181 label="OOCH3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=209 label="Cd_rad/Ct">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=212 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=176 label="O_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=168 label="CH2_triplet">]
[<Entry index=37 label="Cd/H/Ct">, <Entry index=170 label="H_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=212 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=269 label="C_rad/H/CO/Cs">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 29,
    label = "Cd_pri",
    group = 
"""
1 *1 C     0 {2,D} {3,S} {4,S}
2    {C,N} 0 {1,D}
3 *2 H     0 {1,S}
4    H     0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.08316, 'd13': 0.015156, 'd23': -0.068271},
        uncertainties = {'d12': 0.131812, 'd13': 0.077506, 'd23': 0.108519},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 125 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=181 label="OOCH3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=209 label="Cd_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=212 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=168 label="CH2_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=207 label="Cd_rad/Cd">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 459,
    label = "Cd/H2/NonDeC",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.08316, 'd13': 0.015156, 'd23': -0.068271},
        uncertainties = {'d12': 0.131812, 'd13': 0.077506, 'd23': 0.108519},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 125 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=181 label="OOCH3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=209 label="Cd_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=212 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=168 label="CH2_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=207 label="Cd_rad/Cd">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 460,
    label = "Cd/H2/NonDeN",
    group = 
"""
1 *1 C   0 {2,D} {3,S} {4,S}
2    N3d 0 {1,D}
3 *2 H   0 {1,S}
4    H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 30,
    label = "Cd_sec",
    group = 
"""
1 *1 C   0 {2,D} {3,S} {4,S}
2    C   0 {1,D}
3 *2 H   0 {1,S}
4    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.103016, 'd13': 8.8e-05, 'd23': -0.105843},
        uncertainties = {'d12': 0.144116, 'd13': 0.130789, 'd23': 0.119199},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 23 distances.
[<Entry index=35 label="Cd/H/Cd">, <Entry index=232 label="C_methyl">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=170 label="H_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=212 label="Cb_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=37 label="Cd/H/Ct">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=37 label="Cd/H/Ct">, <Entry index=170 label="H_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=176 label="O_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=197 label="Cd_pri_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 31,
    label = "Cd/H/NonDeC",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.129714, 'd13': -0.052554, 'd23': -0.18555},
        uncertainties = {'d12': 0.049871, 'd13': 0.297793, 'd23': 0.288356},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 4 distances.
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=170 label="H_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 32,
    label = "Cd/H/NonDeO",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    O 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 33,
    label = "Cd/H/NonDeS",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 404,
    label = "Cd/H/NonDeN",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    N 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 34,
    label = "Cd/H/OneDe",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2    C                0 {1,D}
3 *2 H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.097806, 'd13': 0.01036, 'd23': -0.090291},
        uncertainties = {'d12': 0.160844, 'd13': 0.122534, 'd23': 0.108547},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 19 distances.
[<Entry index=35 label="Cd/H/Cd">, <Entry index=232 label="C_methyl">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=170 label="H_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=212 label="Cb_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=37 label="Cd/H/Ct">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=37 label="Cd/H/Ct">, <Entry index=170 label="H_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=176 label="O_pri_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=197 label="Cd_pri_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 35,
    label = "Cd/H/Cd",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.116911, 'd13': 0.023009, 'd23': -0.096903},
        uncertainties = {'d12': 0.175923, 'd13': 0.12197, 'd23': 0.115013},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 16 distances.
[<Entry index=35 label="Cd/H/Cd">, <Entry index=232 label="C_methyl">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=170 label="H_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=212 label="Cb_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=176 label="O_pri_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=197 label="Cd_pri_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 36,
    label = "Cd/H/CS",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 37,
    label = "Cd/H/Ct",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Ct 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.025503, 'd13': -0.071285, 'd23': -0.047616},
        uncertainties = {'d12': 0.175238, 'd13': 0.334823, 'd23': 0.201221},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=37 label="Cd/H/Ct">, <Entry index=170 label="H_rad">]
[<Entry index=37 label="Cd/H/Ct">, <Entry index=197 label="Cd_pri_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 38,
    label = "Cd/H/Cb",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 39,
    label = "Cd/H/CO",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *2 H  0 {1,S}
4    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 405,
    label = "Cd/H/N",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
4    N 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 40,
    label = "Cb_H",
    group = 
"""
1 *1 Cb       0 {2,B} {3,B} {4,S}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
4 *2 H        0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.121148, 'd13': 0.031987, 'd23': -0.088308},
        uncertainties = {'d12': 0.112515, 'd13': 0.093749, 'd23': 0.08903},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 29 distances.
[<Entry index=40 label="Cb_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=40 label="Cb_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=40 label="Cb_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=40 label="Cb_H">, <Entry index=176 label="O_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=40 label="Cb_H">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=181 label="OOCH3">]
[<Entry index=40 label="Cb_H">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=170 label="H_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=40 label="Cb_H">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=40 label="Cb_H">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=232 label="C_methyl">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 41,
    label = "CO_H",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
4    R 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.012255, 'd13': 0.058461, 'd23': 0.047233},
        uncertainties = {'d12': 0.053389, 'd13': 0.048795, 'd23': 0.082867},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 129 distances.
[<Entry index=44 label="CO/H/NonDe">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=172 label="O2b">]
[<Entry index=42 label="CO_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=232 label="C_methyl">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=181 label="OOCH3">]
[<Entry index=42 label="CO_pri">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=42 label="CO_pri">, <Entry index=168 label="CH2_triplet">]
[<Entry index=42 label="CO_pri">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=42 label="CO_pri">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=42 label="CO_pri">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=42 label="CO_pri">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=45 label="InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3">, <Entry index=232 label="C_methyl">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=45 label="InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=232 label="C_methyl">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=181 label="OOCH3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=42 label="CO_pri">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=42 label="CO_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=42 label="CO_pri">, <Entry index=170 label="H_rad">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=168 label="CH2_triplet">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=42 label="CO_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=181 label="OOCH3">]
[<Entry index=42 label="CO_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=170 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=232 label="C_methyl">]
[<Entry index=42 label="CO_pri">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H/CdCd">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 42,
    label = "CO_pri",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.014504, 'd13': 0.050605, 'd23': 0.035698},
        uncertainties = {'d12': 0.05609, 'd13': 0.044951, 'd23': 0.079534},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 41 distances.
[<Entry index=42 label="CO_pri">, <Entry index=172 label="O2b">]
[<Entry index=42 label="CO_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=181 label="OOCH3">]
[<Entry index=42 label="CO_pri">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=42 label="CO_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=42 label="CO_pri">, <Entry index=168 label="CH2_triplet">]
[<Entry index=42 label="CO_pri">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=42 label="CO_pri">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=42 label="CO_pri">, <Entry index=232 label="C_methyl">]
[<Entry index=42 label="CO_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=42 label="CO_pri">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=42 label="CO_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=42 label="CO_pri">, <Entry index=170 label="H_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=42 label="CO_pri">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=42 label="CO_pri">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H/CdCd">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 43,
    label = "CO_sec",
    group = 
"""
1 *1 C   0 {2,D} {3,S} {4,S}
2    O   0 {1,D}
3 *2 H   0 {1,S}
4    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.011182, 'd13': 0.062207, 'd23': 0.052733},
        uncertainties = {'d12': 0.053223, 'd13': 0.051344, 'd23': 0.085917},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 88 distances.
[<Entry index=44 label="CO/H/NonDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=232 label="C_methyl">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=45 label="InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3">, <Entry index=232 label="C_methyl">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=45 label="InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=181 label="OOCH3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=168 label="CH2_triplet">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=181 label="OOCH3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=170 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=232 label="C_methyl">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 44,
    label = "CO/H/NonDe",
    group = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2    O        0 {1,D}
3 *2 H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.003464, 'd13': 0.065874, 'd23': 0.062752},
        uncertainties = {'d12': 0.054943, 'd13': 0.057053, 'd23': 0.100835},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 54 distances.
[<Entry index=44 label="CO/H/NonDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=45 label="InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3">, <Entry index=232 label="C_methyl">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=232 label="C_methyl">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=45 label="InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=181 label="OOCH3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=168 label="CH2_triplet">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=170 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=276 label="C_rad/H/CdCd">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 45,
    label = "InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3",
    group = 
"""
1  *1 C 0 {2,D} {3,S} {6,S}
2     O 0 {1,D}
3     C 0 {1,S} {4,S} {7,S} {8,S}
4     C 0 {3,S} {5,S} {9,S} {10,S}
5     C 0 {4,S} {11,S} {12,S} {13,S}
6  *2 H 0 {1,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
11    H 0 {5,S}
12    H 0 {5,S}
13    H 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.031871, 'd13': 0.094771, 'd23': 0.124185},
        uncertainties = {'d12': 0.702038, 'd13': 0.194759, 'd23': 0.856096},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=45 label="InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=45 label="InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3">, <Entry index=232 label="C_methyl">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 46,
    label = "CO/H/OneDe",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2    O                0 {1,D}
3 *2 H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.022419, 'd13': 0.056869, 'd23': 0.038145},
        uncertainties = {'d12': 0.053255, 'd13': 0.043626, 'd23': 0.059905},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 34 distances.
[<Entry index=46 label="CO/H/OneDe">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=181 label="OOCH3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=232 label="C_methyl">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 47,
    label = "CS_H",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    S 0 {1,D}
3 *2 H 0 {1,S}
4    R 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 48,
    label = "CS_pri",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    S 0 {1,D}
3 *2 H 0 {1,S}
4    H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 49,
    label = "CS_sec",
    group = 
"""
1 *1 C   0 {2,D} {3,S} {4,S}
2    S   0 {1,D}
3 *2 H   0 {1,S}
4    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 50,
    label = "CS/H/NonDeC",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    S  0 {1,D}
3 *2 H  0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 51,
    label = "CS/H/NonDeO",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    S 0 {1,D}
3 *2 H 0 {1,S}
4    O 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 52,
    label = "CS/H/NonDeS",
    group = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    S 0 {1,D}
3 *2 H 0 {1,S}
4    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 53,
    label = "CS/H/OneDe",
    group = 
"""
1 *1 C                0 {2,D} {3,S} {4,S}
2    S                0 {1,D}
3 *2 H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 54,
    label = "CS/H/Cd",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    S  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 55,
    label = "CS/H/CS",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    S  0 {1,D}
3 *2 H  0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 56,
    label = "CS/H/Ct",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    S  0 {1,D}
3 *2 H  0 {1,S}
4    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 57,
    label = "CS/H/Cb",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    S  0 {1,D}
3 *2 H  0 {1,S}
4    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 58,
    label = "CS/H/CO",
    group = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2    S  0 {1,D}
3 *2 H  0 {1,S}
4    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 59,
    label = "Cs_H",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
5    R 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.018086, 'd13': 0.036625, 'd23': 0.017619},
        uncertainties = {'d12': 0.051856, 'd13': 0.048754, 'd23': 0.061928},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1036 distances.
[<Entry index=73 label="C/H3/O">, <Entry index=170 label="H_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=145 label="C/H/CdCd">, <Entry index=232 label="C_methyl">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=181 label="OOCH3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=168 label="CH2_triplet">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=212 label="Cb_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=172 label="O2b">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=181 label="OOCH3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=170 label="H_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=73 label="C/H3/O">, <Entry index=181 label="OOCH3">]
[<Entry index=73 label="C/H3/O">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=172 label="O2b">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=212 label="Cb_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=232 label="C_methyl">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=181 label="OOCH3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=212 label="Cb_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=181 label="OOCH3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=170 label="H_rad">]
[<Entry index=60 label="C_methane">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=119 label="C/H/Cs2O">, <Entry index=170 label="H_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=168 label="CH2_triplet">]
[<Entry index=60 label="C_methane">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=72 label="C/H3/CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=168 label="CH2_triplet">]
[<Entry index=72 label="C/H3/CO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=73 label="C/H3/O">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=60 label="C_methane">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=60 label="C_methane">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=60 label="C_methane">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=73 label="C/H3/O">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=181 label="OOCH3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=232 label="C_methyl">]
[<Entry index=73 label="C/H3/O">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=60 label="C_methane">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=172 label="O2b">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=168 label="CH2_triplet">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/CO">, <Entry index=232 label="C_methyl">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=232 label="C_methyl">]
[<Entry index=72 label="C/H3/CO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=73 label="C/H3/O">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=170 label="H_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=168 label="CH2_triplet">]
[<Entry index=60 label="C_methane">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=181 label="OOCH3">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=60 label="C_methane">, <Entry index=176 label="O_pri_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=60 label="C_methane">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=181 label="OOCH3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=170 label="H_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=172 label="O2b">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=73 label="C/H3/O">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=271 label="C_rad/H/OneDeO">]
[<Entry index=60 label="C_methane">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=176 label="O_pri_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=212 label="Cb_rad">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=212 label="Cb_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=212 label="Cb_rad">]
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=73 label="C/H3/O">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=212 label="Cb_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=170 label="H_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=176 label="O_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=181 label="OOCH3">]
[<Entry index=60 label="C_methane">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=170 label="H_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=60 label="C_methane">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=73 label="C/H3/O">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=60 label="C_methane">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=232 label="C_methyl">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=73 label="C/H3/O">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=181 label="OOCH3">]
[<Entry index=73 label="C/H3/O">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=60 label="C_methane">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=176 label="O_pri_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=60 label="C_methane">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=232 label="C_methyl">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=181 label="OOCH3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=168 label="CH2_triplet">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=170 label="H_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=172 label="O2b">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=321 label="C_rad/CdCdCs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=270 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=72 label="C/H3/CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=73 label="C/H3/O">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=212 label="Cb_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=170 label="H_rad">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=172 label="O2b">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=81 label="C/H2/O2">, <Entry index=232 label="C_methyl">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/CO">, <Entry index=172 label="O2b">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=172 label="O2b">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=212 label="Cb_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/CO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=168 label="CH2_triplet">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=73 label="C/H3/O">, <Entry index=172 label="O2b">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=72 label="C/H3/CO">, <Entry index=168 label="CH2_triplet">]
[<Entry index=60 label="C_methane">, <Entry index=212 label="Cb_rad">]
[<Entry index=60 label="C_methane">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=73 label="C/H3/O">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=73 label="C/H3/O">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=232 label="C_methyl">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=232 label="C_methyl">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=170 label="H_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/CO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=232 label="C_methyl">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=72 label="C/H3/CO">, <Entry index=170 label="H_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=93 label="C/H2/OneDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=60 label="C_methane">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=170 label="H_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=60 label="C_methane">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=269 label="C_rad/H/CO/Cs">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 60,
    label = "C_methane",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.084617, 'd13': 0.032934, 'd23': -0.055533},
        uncertainties = {'d12': 0.059795, 'd13': 0.036742, 'd23': 0.041921},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 69 distances.
[<Entry index=60 label="C_methane">, <Entry index=212 label="Cb_rad">]
[<Entry index=60 label="C_methane">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=60 label="C_methane">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=60 label="C_methane">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=60 label="C_methane">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=170 label="H_rad">]
[<Entry index=60 label="C_methane">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=60 label="C_methane">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=181 label="OOCH3">]
[<Entry index=60 label="C_methane">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=60 label="C_methane">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=60 label="C_methane">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=60 label="C_methane">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=60 label="C_methane">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=60 label="C_methane">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=60 label="C_methane">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=60 label="C_methane">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=60 label="C_methane">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=60 label="C_methane">, <Entry index=321 label="C_rad/CdCdCs">]
[<Entry index=60 label="C_methane">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=60 label="C_methane">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=60 label="C_methane">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=60 label="C_methane">, <Entry index=176 label="O_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=256 label="C_rad/H/CsO">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 61,
    label = "C_pri",
    group = 
"""
1 *1 C   0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   0 {1,S}
3    H   0 {1,S}
4    H   0 {1,S}
5    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.03527, 'd13': 0.029355, 'd23': -0.007283},
        uncertainties = {'d12': 0.050659, 'd13': 0.037729, 'd23': 0.052535},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 543 distances.
[<Entry index=73 label="C/H3/O">, <Entry index=170 label="H_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=73 label="C/H3/O">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=73 label="C/H3/O">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=170 label="H_rad">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=212 label="Cb_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=172 label="O2b">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=176 label="O_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/CO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/CO">, <Entry index=232 label="C_methyl">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=170 label="H_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=73 label="C/H3/O">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=73 label="C/H3/O">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=73 label="C/H3/O">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=73 label="C/H3/O">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=271 label="C_rad/H/OneDeO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=172 label="O2b">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=170 label="H_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=168 label="CH2_triplet">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=73 label="C/H3/O">, <Entry index=181 label="OOCH3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=212 label="Cb_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=181 label="OOCH3">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=73 label="C/H3/O">, <Entry index=232 label="C_methyl">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=72 label="C/H3/CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=168 label="CH2_triplet">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=172 label="O2b">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=181 label="OOCH3">]
[<Entry index=73 label="C/H3/O">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=73 label="C/H3/O">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=168 label="CH2_triplet">]
[<Entry index=72 label="C/H3/CO">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=212 label="Cb_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=172 label="O2b">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=72 label="C/H3/CO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=73 label="C/H3/O">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=232 label="C_methyl">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=168 label="CH2_triplet">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=176 label="O_pri_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=73 label="C/H3/O">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=72 label="C/H3/CO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=232 label="C_methyl">]
[<Entry index=72 label="C/H3/CO">, <Entry index=181 label="OOCH3">]
[<Entry index=73 label="C/H3/O">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=172 label="O2b">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=232 label="C_methyl">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=181 label="OOCH3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=170 label="H_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=72 label="C/H3/CO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=73 label="C/H3/O">, <Entry index=168 label="CH2_triplet">]
[<Entry index=72 label="C/H3/CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/CO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=232 label="C_methyl">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=73 label="C/H3/O">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=170 label="H_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=212 label="Cb_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/CO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=73 label="C/H3/O">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=73 label="C/H3/O">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=270 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=72 label="C/H3/CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=217 label="CO_rad/OneDe">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 62,
    label = "C/H3/Cs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.061543, 'd13': 0.026123, 'd23': -0.038291},
        uncertainties = {'d12': 0.046777, 'd13': 0.036361, 'd23': 0.047037},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 277 distances.
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=232 label="C_methyl">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=271 label="C_rad/H/OneDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=176 label="O_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=170 label="H_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=270 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=168 label="CH2_triplet">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=212 label="Cb_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=212 label="Cb_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=176 label="O_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=181 label="OOCH3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=311 label="C_rad/COCs2">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 63,
    label = "InChI=1/C2H6/c1-2/h1-2H3",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {2,S}
7    H 0 {2,S}
8    H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.057546, 'd13': 0.0318, 'd23': -0.029222},
        uncertainties = {'d12': 0.056345, 'd13': 0.036156, 'd23': 0.051725},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 57 distances.
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=271 label="C_rad/H/OneDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=176 label="O_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=212 label="Cb_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=270 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=250 label="C_rad/H/NonDeC">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 64,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/gamma",
    group = 
"""
1  *1 C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {5,S} {9,S}
3     C 0 {2,S} {4,S} {10,S} {11,S}
4     O 0 {3,S} {12,S}
5     C 0 {2,S} {13,S} {14,S} {15,S}
6  *2 H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
15    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 65,
    label = "C/H3/Cd",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.009436, 'd13': 0.042023, 'd23': 0.049109},
        uncertainties = {'d12': 0.056721, 'd13': 0.045186, 'd23': 0.068026},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 128 distances.
[<Entry index=65 label="C/H3/Cd">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=170 label="H_rad">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=232 label="C_methyl">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=212 label="Cb_rad">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=232 label="C_methyl">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=172 label="O2b">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=232 label="C_methyl">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=181 label="OOCH3">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=172 label="O2b">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=168 label="CH2_triplet">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=170 label="H_rad">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=172 label="O2b">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=246 label="C_rad/H2/CO">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 66,
    label = "C/H3/CS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S} {6,D}
6    S  0 {5,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 67,
    label = "InChI=1/C3H6/c1-3-2/h3H,1H2,2H3",
    group = 
"""
1 *1 C 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 {1,S} {3,D} {7,S}
3    C 0 {2,D} {8,S} {9,S}
4 *2 H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {3,S}
9    H 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.01234, 'd13': 0.032657, 'd23': 0.042815},
        uncertainties = {'d12': 0.04144, 'd13': 0.03525, 'd23': 0.036938},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 39 distances.
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=170 label="H_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=172 label="O2b">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=246 label="C_rad/H2/CO">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 68,
    label = "InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3",
    group = 
"""
1     C 0 {2,D} {5,S} {6,S}
2     C 0 {1,D} {3,S} {4,S}
3  *1 C 0 {2,S} {7,S} {8,S} {9,S}
4     C 0 {2,S} {10,S} {11,S} {12,S}
5     H 0 {1,S}
6     H 0 {1,S}
7  *2 H 0 {3,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {4,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.019388, 'd13': 0.01514, 'd23': 0.029828},
        uncertainties = {'d12': 0.090489, 'd13': 0.189569, 'd23': 0.109129},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=232 label="C_methyl">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=172 label="O2b">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=178 label="O_rad/NonDeC">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 69,
    label = "InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+",
    group = 
"""
1  *1 C 0 {2,S} {5,S} {6,S} {7,S}
2     C 0 {1,S} {3,D} {8,S}
3     C 0 {2,D} {4,S} {9,S}
4     C 0 {3,S} {10,S} {11,S} {12,S}
5     H 0 {1,S}
6     H 0 {1,S}
7  *2 H 0 {1,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {4,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.038388, 'd13': 0.037897, 'd23': 0.072724},
        uncertainties = {'d12': 0.114472, 'd13': 0.159249, 'd23': 0.075254},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=232 label="C_methyl">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 70,
    label = "C/H3/Ct",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Ct 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.010743, 'd13': 0.026852, 'd23': 0.012939},
        uncertainties = {'d12': 0.050607, 'd13': 0.028479, 'd23': 0.05227},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 27 distances.
[<Entry index=70 label="C/H3/Ct">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=181 label="OOCH3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=168 label="CH2_triplet">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=170 label="H_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=214 label="CO_pri_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 71,
    label = "C/H3/Cb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 72,
    label = "C/H3/CO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    CO 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.031482, 'd13': 0.020023, 'd23': -0.009339},
        uncertainties = {'d12': 0.062489, 'd13': 0.037209, 'd23': 0.047},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 63 distances.
[<Entry index=72 label="C/H3/CO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=72 label="C/H3/CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=72 label="C/H3/CO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=172 label="O2b">]
[<Entry index=72 label="C/H3/CO">, <Entry index=170 label="H_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=181 label="OOCH3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/CO">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/CO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/CO">, <Entry index=232 label="C_methyl">]
[<Entry index=72 label="C/H3/CO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=72 label="C/H3/CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=168 label="CH2_triplet">]
[<Entry index=72 label="C/H3/CO">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=72 label="C/H3/CO">, <Entry index=311 label="C_rad/COCs2">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 73,
    label = "C/H3/O",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    O 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.03144, 'd13': 0.025746, 'd23': 0.00088},
        uncertainties = {'d12': 0.045404, 'd13': 0.033577, 'd23': 0.04991},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 48 distances.
[<Entry index=73 label="C/H3/O">, <Entry index=170 label="H_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=73 label="C/H3/O">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=73 label="C/H3/O">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=73 label="C/H3/O">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=73 label="C/H3/O">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=73 label="C/H3/O">, <Entry index=212 label="Cb_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=181 label="OOCH3">]
[<Entry index=73 label="C/H3/O">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=73 label="C/H3/O">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=73 label="C/H3/O">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=73 label="C/H3/O">, <Entry index=232 label="C_methyl">]
[<Entry index=73 label="C/H3/O">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=73 label="C/H3/O">, <Entry index=172 label="O2b">]
[<Entry index=73 label="C/H3/O">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=73 label="C/H3/O">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=73 label="C/H3/O">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=73 label="C/H3/O">, <Entry index=168 label="CH2_triplet">]
[<Entry index=73 label="C/H3/O">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=73 label="C/H3/O">, <Entry index=241 label="C_rad/H2/Cd">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 74,
    label = "C/H3/S",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 461,
    label = "Cs/H3/NonDeN",
    group = 
"""
1 *1 C   0 {2,S} {3,S} {4,S} {5,S}
2    N3s 0 {1,S}
3 *2 H   0 {1,S}
4    H   0 {1,S}
5    H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 471,
    label = "Cs/H3/OneDeN",
    group = 
"""
1 *1 C         0 {2,S} {3,S} {4,S} {5,S}
2    {N3d,N5d} 0 {1,S}
3 *2 H         0 {1,S}
4    H         0 {1,S}
5    H         0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 75,
    label = "C_sec",
    group = 
"""
1 *1 C   0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   0 {1,S}
3    H   0 {1,S}
4    R!H 0 {1,S}
5    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.014198, 'd13': 0.046289, 'd23': 0.060329},
        uncertainties = {'d12': 0.054366, 'd13': 0.058313, 'd23': 0.075538},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 333 distances.
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=212 label="Cb_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=181 label="OOCH3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=170 label="H_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=168 label="CH2_triplet">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=81 label="C/H2/O2">, <Entry index=232 label="C_methyl">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=93 label="C/H2/OneDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=232 label="C_methyl">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=172 label="O2b">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=232 label="C_methyl">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=170 label="H_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=170 label="H_rad">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=212 label="Cb_rad">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=181 label="OOCH3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=232 label="C_methyl">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=170 label="H_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=181 label="OOCH3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=168 label="CH2_triplet">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=172 label="O2b">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=212 label="Cb_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=232 label="C_methyl">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 76,
    label = "C/H2/NonDeC",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.03798, 'd13': 0.013546, 'd23': -0.027677},
        uncertainties = {'d12': 0.055505, 'd13': 0.032625, 'd23': 0.051286},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 62 distances.
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=212 label="Cb_rad">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=172 label="O2b">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=168 label="CH2_triplet">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 77,
    label = "InChI=1/C3H8/c1-3-2/h3H2,1-2H3",
    group = 
"""
1     C 0 {2,S} {4,S} {5,S} {6,S}
2  *1 C 0 {1,S} {3,S} {7,S} {8,S}
3     C 0 {2,S} {9,S} {10,S} {11,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {1,S}
7  *2 H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.051887, 'd13': 0.035285, 'd23': -0.019615},
        uncertainties = {'d12': 0.052108, 'd13': 0.032381, 'd23': 0.038476},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 42 distances.
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=172 label="O2b">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=168 label="CH2_triplet">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 78,
    label = "C/H2/NonDeO",
    group = 
"""
1 *1 C        0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        0 {1,S}
3    H        0 {1,S}
4    O        0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.02416, 'd13': 0.029179, 'd23': 0.012412},
        uncertainties = {'d12': 0.056252, 'd13': 0.044489, 'd23': 0.075571},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 43 distances.
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=181 label="OOCH3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=170 label="H_rad">]
[<Entry index=81 label="C/H2/O2">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 79,
    label = "C/H2/CsO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    O  0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.023479, 'd13': 0.029541, 'd23': 0.013805},
        uncertainties = {'d12': 0.056104, 'd13': 0.045167, 'd23': 0.075296},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 41 distances.
[<Entry index=79 label="C/H2/CsO">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=181 label="OOCH3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=170 label="H_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 80,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha",
    group = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {5,S} {9,S}
3  *1 C 0 {2,S} {4,S} {10,S} {11,S}
4     O 0 {3,S} {12,S}
5     C 0 {2,S} {13,S} {14,S} {15,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10 *2 H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
15    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 81,
    label = "C/H2/O2",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S}
5    O 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.039134, 'd13': 0.02122, 'd23': -0.018219},
        uncertainties = {'d12': 0.540322, 'd13': 0.264782, 'd23': 0.738404},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=81 label="C/H2/O2">, <Entry index=232 label="C_methyl">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 82,
    label = "C/H2/NonDeS",
    group = 
"""
1 *1 C        0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        0 {1,S}
3    H        0 {1,S}
4    S        0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 83,
    label = "C/H2/CsS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 407,
    label = "C/H2/NonDeN",
    group = 
"""
1 *1 C          0 {2,S} {3,S} {4,S} {5,S}
2 *2 H          0 {1,S}
3    H          0 {1,S}
4    N          0 {1,S}
5    {Cs,O,S,N} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 84,
    label = "C/H2/OneDe",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    H                0 {1,S}
4    {Cd,Ct,CO,Cb,CS} 0 {1,S}
5    {Cs,O,S}         0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.02435, 'd13': 0.049652, 'd23': 0.073236},
        uncertainties = {'d12': 0.056484, 'd13': 0.05523, 'd23': 0.076114},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 143 distances.
[<Entry index=86 label="C/H2/CdCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=93 label="C/H2/OneDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=170 label="H_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=172 label="O2b">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=170 label="H_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=168 label="CH2_triplet">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=212 label="Cb_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=232 label="C_methyl">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=181 label="OOCH3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=232 label="C_methyl">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 85,
    label = "C/H2/OneDeC",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    H                0 {1,S}
4    {Cd,Ct,CO,Cb,CS} 0 {1,S}
5    Cs               0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.024137, 'd13': 0.049492, 'd23': 0.072849},
        uncertainties = {'d12': 0.056588, 'd13': 0.055398, 'd23': 0.076233},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 142 distances.
[<Entry index=86 label="C/H2/CdCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=170 label="H_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=172 label="O2b">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=170 label="H_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=168 label="CH2_triplet">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=212 label="Cb_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=232 label="C_methyl">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=181 label="OOCH3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=232 label="C_methyl">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 86,
    label = "C/H2/CdCs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.031459, 'd13': 0.052433, 'd23': 0.082469},
        uncertainties = {'d12': 0.056371, 'd13': 0.059648, 'd23': 0.080689},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 117 distances.
[<Entry index=86 label="C/H2/CdCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=172 label="O2b">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=170 label="H_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=168 label="CH2_triplet">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=212 label="Cb_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=232 label="C_methyl">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=181 label="OOCH3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=269 label="C_rad/H/CO/Cs">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 87,
    label = "C/H2/CSCs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S} {6,D}
5    Cs 0 {1,S}
6    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 88,
    label = "C/H2/CtCs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 89,
    label = "C/H2/CbCs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 90,
    label = "C/H2/COCs",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    CO 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.009958, 'd13': 0.035794, 'd23': 0.028052},
        uncertainties = {'d12': 0.06186, 'd13': 0.031287, 'd23': 0.055159},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 25 distances.
[<Entry index=90 label="C/H2/COCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=232 label="C_methyl">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=170 label="H_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=256 label="C_rad/H/CsO">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 91,
    label = "InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3/beta",
    group = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2  *1 C 0 {1,S} {3,S} {8,S} {9,S}
3     C 0 {2,S} {4,D} {10,S}
4     O 0 {3,D}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8  *2 H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 92,
    label = "InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3",
    group = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2  *1 C 0 {1,S} {3,S} {8,S} {9,S}
3     C 0 {2,S} {4,D} {10,S}
4     C 0 {3,D} {11,S} {12,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8  *2 H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 93,
    label = "C/H2/OneDeO",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    H                0 {1,S}
4    {Cd,Ct,CO,Cb,CS} 0 {1,S}
5    O                0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.051805, 'd13': 0.070402, 'd23': 0.123143},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=93 label="C/H2/OneDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 94,
    label = "C/H2/OneDeS",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    H                0 {1,S}
4    {Cd,Ct,CO,Cb,CS} 0 {1,S}
5    S                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 95,
    label = "C/H2/CdS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    S  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 96,
    label = "C/H2/CtS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    S  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 97,
    label = "C/H2/TwoDe",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    H                0 {1,S}
4    {Cd,Ct,CO,Cb,CS} 0 {1,S}
5    {Cd,Ct,CO,Cb,CS} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.050458, 'd13': 0.070648, 'd23': 0.120266},
        uncertainties = {'d12': 0.052264, 'd13': 0.082408, 'd23': 0.092058},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 85 distances.
[<Entry index=98 label="C/H2/CdCd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=181 label="OOCH3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=170 label="H_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=168 label="CH2_triplet">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=232 label="C_methyl">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=212 label="Cb_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 98,
    label = "C/H2/CdCd",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cd 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.050458, 'd13': 0.070648, 'd23': 0.120266},
        uncertainties = {'d12': 0.052264, 'd13': 0.082408, 'd23': 0.092058},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 85 distances.
[<Entry index=98 label="C/H2/CdCd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=181 label="OOCH3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=170 label="H_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=168 label="CH2_triplet">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=232 label="C_methyl">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=212 label="Cb_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 99,
    label = "C/H2/CdCS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cd 0 {1,S} {6,D}
6    S  0 {5,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 100,
    label = "C/H2/CSCS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S} {6,D}
5    Cd 0 {1,S} {7,D}
6    S  0 {4,D}
7    S  0 {5,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 101,
    label = "C/H2/CdCt",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 102,
    label = "C/H2/CtCS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Cd 0 {1,S} {6,D}
6    S  0 {5,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 103,
    label = "C/H2/CdCb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 104,
    label = "C/H2/CbCS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
5    Cd 0 {1,S} {6,D}
6    S  0 {5,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 105,
    label = "C/H2/CdCO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
5    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 106,
    label = "C/H2/COCS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    CO 0 {1,S}
5    Cd 0 {1,S} {6,D}
6    S  0 {5,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 107,
    label = "C/H2/CtCt",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 108,
    label = "C/H2/CtCb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 109,
    label = "C/H2/CtCO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
5    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 110,
    label = "C/H2/CbCb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
5    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 111,
    label = "C/H2/CbCO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
5    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 112,
    label = "C/H2/COCO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    CO 0 {1,S}
5    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 113,
    label = "C/H2/Cb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    C  0 {1,S}
5    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 114,
    label = "C_ter",
    group = 
"""
1 *1 C   0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
5    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.01475, 'd13': 0.046663, 'd23': 0.062582},
        uncertainties = {'d12': 0.045737, 'd13': 0.073795, 'd23': 0.073633},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 91 distances.
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=176 label="O_pri_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=168 label="CH2_triplet">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=181 label="OOCH3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=232 label="C_methyl">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=172 label="O2b">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=145 label="C/H/CdCd">, <Entry index=232 label="C_methyl">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=212 label="Cb_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=212 label="Cb_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=170 label="H_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=172 label="O2b">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=119 label="C/H/Cs2O">, <Entry index=170 label="H_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=181 label="OOCH3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=180 label="O_rad/NonDeO">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 115,
    label = "C/H/NonDeC",
    group = 
"""
1 *1 C        0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        0 {1,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.009086, 'd13': 0.013026, 'd23': 0.001879},
        uncertainties = {'d12': 0.059382, 'd13': 0.145324, 'd23': 0.13474},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 16 distances.
[<Entry index=116 label="C/H/Cs3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=170 label="H_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=212 label="Cb_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=119 label="C/H/Cs2O">, <Entry index=170 label="H_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=181 label="OOCH3">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=172 label="O2b">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 116,
    label = "C/H/Cs3",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.01469, 'd13': 0.020459, 'd23': 0.00377},
        uncertainties = {'d12': 0.059739, 'd13': 0.052238, 'd23': 0.059322},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 15 distances.
[<Entry index=116 label="C/H/Cs3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=170 label="H_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=212 label="Cb_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=181 label="OOCH3">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=172 label="O2b">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 117,
    label = "InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta",
    group = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *1 C 0 {1,S} {3,S} {5,S} {9,S}
3     C 0 {2,S} {4,S} {10,S} {11,S}
4     O 0 {3,S} {12,S}
5     C 0 {2,S} {13,S} {14,S} {15,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9  *2 H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
15    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 408,
    label = "C/H/Cs2N",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    N  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 118,
    label = "C/H/NDMustO",
    group = 
"""
1 *1 C      0 {2,S} {3,S} {4,S} {5,S}
2 *2 H      0 {1,S}
3    O      0 {1,S}
4    {Cs,O} 0 {1,S}
5    {Cs,O} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.12541, 'd13': -0.165364, 'd23': -0.043501},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=119 label="C/H/Cs2O">, <Entry index=170 label="H_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 119,
    label = "C/H/Cs2O",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    O  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.12541, 'd13': -0.165364, 'd23': -0.043501},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=119 label="C/H/Cs2O">, <Entry index=170 label="H_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 120,
    label = "C/H/CsO2",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    O  0 {1,S}
4    O  0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 121,
    label = "C/H/O3",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    O 0 {1,S}
4    O 0 {1,S}
5    O 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 122,
    label = "C/H/NDMustS",
    group = 
"""
1 *1 C      0 {2,S} {3,S} {4,S} {5,S}
2 *2 H      0 {1,S}
3    S      0 {1,S}
4    {Cs,S} 0 {1,S}
5    {Cs,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 123,
    label = "C/H/Cs2S",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 124,
    label = "C/H/CsS2",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    S  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 125,
    label = "C/H/S3",
    group = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    S 0 {1,S}
4    S 0 {1,S}
5    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 126,
    label = "C/H/NDMustOS",
    group = 
"""
1 *1 C        0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        0 {1,S}
3    O        0 {1,S}
4    S        0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 127,
    label = "C/H/CsOS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    O  0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 128,
    label = "C/H/OneDe",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cs,O,S}         0 {1,S}
5    {Cs,O,S}         0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.01833, 'd13': 0.051967, 'd23': 0.072129},
        uncertainties = {'d12': 0.042956, 'd13': 0.054311, 'd23': 0.057235},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 74 distances.
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=176 label="O_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=168 label="CH2_triplet">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=212 label="Cb_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=172 label="O2b">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=232 label="C_methyl">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=181 label="OOCH3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 129,
    label = "C/H/Cs2",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
5    Cs               0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.01833, 'd13': 0.051967, 'd23': 0.072129},
        uncertainties = {'d12': 0.042956, 'd13': 0.054311, 'd23': 0.057235},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 74 distances.
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=176 label="O_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=168 label="CH2_triplet">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=212 label="Cb_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=172 label="O2b">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=232 label="C_methyl">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=181 label="OOCH3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 130,
    label = "C/H/Cs2Cd",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 131,
    label = "C/H/Cs2CS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S} {6,D}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
6    S  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 132,
    label = "C/H/Cs2Ct",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 133,
    label = "C/H/Cs2Cb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 134,
    label = "C/H/Cs2CO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    CO 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.01833, 'd13': 0.051967, 'd23': 0.072129},
        uncertainties = {'d12': 0.042956, 'd13': 0.054311, 'd23': 0.057235},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 74 distances.
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=176 label="O_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=168 label="CH2_triplet">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=212 label="Cb_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=172 label="O2b">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=232 label="C_methyl">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=181 label="OOCH3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 135,
    label = "InChI=1/C4H8O/c1-4(2)3-5/h3-4H,1-2H3",
    group = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *1 C 0 {1,S} {3,S} {5,S} {9,S}
3     C 0 {2,S} {4,D} {10,S}
4     O 0 {3,D}
5     C 0 {2,S} {11,S} {12,S} {13,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9  *2 H 0 {2,S}
10    H 0 {3,S}
11    H 0 {5,S}
12    H 0 {5,S}
13    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 136,
    label = "C/H/CsO",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    O                0 {1,S}
5    Cs               0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 137,
    label = "C/H/CsS",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    S                0 {1,S}
5    Cs               0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 138,
    label = "C/H/CdCsS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 139,
    label = "C/H/CtCsS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 140,
    label = "C/H/OO",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    O                0 {1,S}
5    O                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 141,
    label = "C/H/OS",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    O                0 {1,S}
5    S                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 142,
    label = "C/H/SS",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    S                0 {1,S}
5    S                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 143,
    label = "C/H/TwoDe",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cs,O,S}         0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.112605, 'd13': 0.160149, 'd23': 0.269965},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=145 label="C/H/CdCd">, <Entry index=232 label="C_methyl">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 144,
    label = "C/H/Cs",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    Cs               0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.112605, 'd13': 0.160149, 'd23': 0.269965},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=145 label="C/H/CdCd">, <Entry index=232 label="C_methyl">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 145,
    label = "C/H/CdCd",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.112605, 'd13': 0.160149, 'd23': 0.269965},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=145 label="C/H/CdCd">, <Entry index=232 label="C_methyl">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 146,
    label = "C/H/CdCS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S} {6,D}
5    Cs 0 {1,S}
6    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 147,
    label = "C/H/CSCS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S} {6,D}
4    Cd 0 {1,S} {7,D}
5    Cs 0 {1,S}
6    S  0 {3,D}
7    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 148,
    label = "C/H/CdCt",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 149,
    label = "C/H/CtCS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Cd 0 {1,S} {6,D}
5    Cs 0 {1,S}
6    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 150,
    label = "C/H/CdCb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    Cb 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 151,
    label = "C/H/CbCS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
4    Cd 0 {1,S} {6,D}
5    Cs 0 {1,S}
6    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 152,
    label = "C/H/CdCO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cd 0 {1,S}
4    CO 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 153,
    label = "C/H/COCS",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    CO 0 {1,S}
4    Cd 0 {1,S} {6,D}
5    Cs 0 {1,S}
6    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 154,
    label = "C/H/CtCt",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 155,
    label = "C/H/CtCb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    Cb 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 156,
    label = "C/H/CtCO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Ct 0 {1,S}
4    CO 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 157,
    label = "C/H/CbCb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
4    Cb 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 158,
    label = "C/H/CbCO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    Cb 0 {1,S}
4    CO 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 159,
    label = "C/H/COCO",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    CO 0 {1,S}
4    CO 0 {1,S}
5    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 160,
    label = "C/H/TDMustO",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    O                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 161,
    label = "C/H/TDMustS",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    S                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 162,
    label = "C/H/ThreeDe",
    group = 
"""
1 *1 C                0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 163,
    label = "C/H/Cb",
    group = 
"""
1 *1 C  0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  0 {1,S}
3    C  0 {1,S}
4    C  0 {1,S}
5    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 164,
    label = "Xrad_H",
    group = 
"""
1 *1 R 1 {2,S}
2 *2 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.087089, 'd13': -0.015098, 'd23': -0.105155},
        uncertainties = {'d12': 0.095352, 'd13': 0.075048, 'd23': 0.074861},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 47 distances.
[<Entry index=442 label="CH3_rad_H">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=443 label="OH_rad_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=443 label="OH_rad_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=443 label="OH_rad_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=170 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=443 label="OH_rad_H">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=443 label="OH_rad_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=443 label="OH_rad_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=443 label="OH_rad_H">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=443 label="OH_rad_H">, <Entry index=232 label="C_methyl">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=265 label="C_rad/H/CdCs">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 469,
    label = "C_rad_H",
    group = 
"""
1 *1 C 1 {2,S}
2 *2 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.162209, 'd13': 0.046524, 'd23': -0.118775},
        uncertainties = {'d12': 0.089765, 'd13': 0.090444, 'd23': 0.040857},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 31 distances.
[<Entry index=442 label="CH3_rad_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=170 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=265 label="C_rad/H/CdCs">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 442,
    label = "CH3_rad_H",
    group = 
"""
1 *1 Cs 1 {2,S} {3,S} {4,S}
2 *2 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.162209, 'd13': 0.046524, 'd23': -0.118775},
        uncertainties = {'d12': 0.089765, 'd13': 0.090444, 'd23': 0.040857},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 31 distances.
[<Entry index=442 label="CH3_rad_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=170 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=265 label="C_rad/H/CdCs">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 470,
    label = "Cs/H2/OneDeN",
    group = 
"""
1 *1 C         1 {2,S} {3,S} {4,S}
2 *2 H         0 {1,S}
3    H         0 {1,S}
4    {N3d,N5d} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 443,
    label = "OH_rad_H",
    group = 
"""
1 *1 O 1 {2,S}
2 *2 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.064055, 'd13': -0.139084, 'd23': -0.077752},
        uncertainties = {'d12': 0.117088, 'd13': 0.039323, 'd23': 0.125034},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 16 distances.
[<Entry index=443 label="OH_rad_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=443 label="OH_rad_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=443 label="OH_rad_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=443 label="OH_rad_H">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=443 label="OH_rad_H">, <Entry index=232 label="C_methyl">]
[<Entry index=443 label="OH_rad_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=207 label="Cd_rad/Cd">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 165,
    label = "Srad_H",
    group = 
"""
1 *1 S 1 {2,S}
2 *2 H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 416,
    label = "N3s_rad_H",
    group = 
"""
1 *1 N3s 1 {2,S}
2 *2 H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 417,
    label = "NH2_rad_H",
    group = 
"""
1 *1 N3s 1 {2,S} {3,S}
2 *2 H   0 {1,S}
3    H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 418,
    label = "N3s_rad_H_pri",
    group = 
"""
1 *1 N3s     1 {2,S} {3,S}
2 *2 H       0 {1,S}
3    {C,N,O} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 449,
    label = "N3s_rad_H/H/NonDeN",
    group = 
"""
1 *1 N3s 1 {2,S} {3,S}
2 *2 H   0 {1,S}
3    N3s 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 444,
    label = "Xbirad_H",
    group = "OR{CH2_triplet_H, CH2_singlet_H, NH_triplet_H, NH_singlet_H}",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 478,
    label = "NH_triplet_H",
    group = 
"""
1 *1 N 2T {2,S}
2 *2 H 0  {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 479,
    label = "NH_singlet_H",
    group = 
"""
1 *1 N 2S {2,S}
2 *2 H 0  {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 476,
    label = "CH2_triplet_H",
    group = 
"""
1 *1 C 2T {2,S} {3,S}
2 *2 H 0  {1,S}
3    H 0  {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 477,
    label = "CH2_singlet_H",
    group = 
"""
1 *1 C 2S {2,S} {3,S}
2 *2 H 0  {1,S}
3    H 0  {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 474,
    label = "Xtrirad_H",
    group = "OR{C_quartet_H, C_doublet_H}",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 480,
    label = "C_quartet_H",
    group = 
"""
1 *1 C 3Q {2,S}
2 *2 H 0  {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 481,
    label = "C_doublet_H",
    group = 
"""
1 *1 C 3D {2,S}
2 *2 H 0  {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 475,
    label = "Y_1centerquadrad",
    group = "OR{C_quintet, C_triplet, C_singlet}",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 482,
    label = "C_quintet",
    group = 
"""
1 *3 C 4V
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 483,
    label = "C_triplet",
    group = 
"""
1 *3 C 4T
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 484,
    label = "C_singlet",
    group = 
"""
1 *3 C 4S
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 419,
    label = "Y_1centertrirad",
    group = "OR{N_atom_quartet, N_atom_doublet, CH_quartet, CH_doublet}",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 485,
    label = "N_atom_quartet",
    group = 
"""
1 *3 N 3Q
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 486,
    label = "N_atom_doublet",
    group = 
"""
1 *3 N 3D
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 487,
    label = "CH_quartet",
    group = 
"""
1 *3 C 3Q {2,S}
2    H 0  {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 487,
    label = "CH_doublet",
    group = 
"""
1 *3 C 3D {2,S}
2    H 0  {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 166,
    label = "Y_1centerbirad",
    group = 
"""
1 *3 R!H {2S,2T}
""",
    distances = DistanceData(
        distances = {'d12': -0.105744, 'd13': -0.016072, 'd23': 0.086669},
        uncertainties = {'d12': 0.074043, 'd13': 0.075038, 'd23': 0.096478},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 47 distances.
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=168 label="CH2_triplet">]
[<Entry index=72 label="C/H3/CO">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=4 label="H2">, <Entry index=168 label="CH2_triplet">]
[<Entry index=42 label="CO_pri">, <Entry index=168 label="CH2_triplet">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=168 label="CH2_triplet">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=168 label="CH2_triplet">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=168 label="CH2_triplet">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=168 label="CH2_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=168 label="CH2_triplet">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=168 label="CH2_triplet">]
[<Entry index=73 label="C/H3/O">, <Entry index=168 label="CH2_triplet">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=168 label="CH2_triplet">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=168 label="CH2_triplet">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=168 label="CH2_triplet">]
[<Entry index=60 label="C_methane">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=73 label="C/H3/O">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=72 label="C/H3/CO">, <Entry index=168 label="CH2_triplet">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 167,
    label = "O_atom_triplet",
    group = 
"""
1 *3 O 2T
""",
    distances = DistanceData(
        distances = {'d12': -0.080049, 'd13': -0.139384, 'd23': -0.062069},
        uncertainties = {'d12': 0.122327, 'd13': 0.039628, 'd23': 0.114786},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 16 distances.
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=73 label="C/H3/O">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=72 label="C/H3/CO">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=60 label="C_methane">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=167 label="O_atom_triplet">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=167 label="O_atom_triplet">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 488,
    label = "O_atom_singlet",
    group = 
"""
1 *3 O 2S
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 422,
    label = "NH_triplet",
    group = 
"""
1 *3 N3s 2T {2,s}
2    H   0  {1,s}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 490,
    label = "NH_singlet",
    group = 
"""
1 *3 N 2S {2,S}
2    H 0  {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 168,
    label = "CH2_triplet",
    group = 
"""
1 *3 C 2T {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.118667, 'd13': 0.045948, 'd23': 0.161478},
        uncertainties = {'d12': 0.042244, 'd13': 0.09037, 'd23': 0.092971},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 31 distances.
[<Entry index=11 label="H2O2">, <Entry index=168 label="CH2_triplet">]
[<Entry index=4 label="H2">, <Entry index=168 label="CH2_triplet">]
[<Entry index=42 label="CO_pri">, <Entry index=168 label="CH2_triplet">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=168 label="CH2_triplet">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=168 label="CH2_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=168 label="CH2_triplet">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=168 label="CH2_triplet">]
[<Entry index=73 label="C/H3/O">, <Entry index=168 label="CH2_triplet">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=168 label="CH2_triplet">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=168 label="CH2_triplet">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=168 label="CH2_triplet">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=168 label="CH2_triplet">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=168 label="CH2_triplet">]
[<Entry index=72 label="C/H3/CO">, <Entry index=168 label="CH2_triplet">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=168 label="CH2_triplet">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 489,
    label = "CH2_singlet",
    group = 
"""
1 *3 C 2S {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 169,
    label = "Y_rad",
    group = 
"""
1 *3 R 1
""",
    distances = DistanceData(
        distances = {'d12': 0.003207, 'd13': 0.000487, 'd23': -0.002629},
        uncertainties = {'d12': 0.080517, 'd13': 0.066625, 'd23': 0.077801},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1601 distances.
[<Entry index=44 label="CO/H/NonDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=73 label="C/H3/O">, <Entry index=170 label="H_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=37 label="Cd/H/Ct">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=176 label="O_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=212 label="Cb_rad">]
[<Entry index=145 label="C/H/CdCd">, <Entry index=232 label="C_methyl">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=181 label="OOCH3">]
[<Entry index=42 label="CO_pri">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=212 label="Cb_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=172 label="O2b">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=42 label="CO_pri">, <Entry index=172 label="O2b">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=45 label="InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3">, <Entry index=232 label="C_methyl">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=181 label="OOCH3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=4 label="H2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=172 label="O2b">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=170 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/CO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=119 label="C/H/Cs2O">, <Entry index=170 label="H_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=73 label="C/H3/O">, <Entry index=181 label="OOCH3">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=73 label="C/H3/O">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=11 label="H2O2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=4 label="H2">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=172 label="O2b">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=212 label="Cb_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=212 label="Cb_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=172 label="O2b">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=212 label="Cb_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=232 label="C_methyl">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=181 label="OOCH3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=296 label="C_rad/Cs2O">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=181 label="OOCH3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=181 label="OOCH3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=170 label="H_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=7 label="O_pri">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=60 label="C_methane">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=40 label="Cb_H">, <Entry index=181 label="OOCH3">]
[<Entry index=13 label="ROOH_sec">, <Entry index=172 label="O2b">]
[<Entry index=12 label="ROOH_pri">, <Entry index=212 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=203 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=181 label="OOCH3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=73 label="C/H3/O">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=232 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=11 label="H2O2">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=45 label="InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=14 label="ROOH_ter">, <Entry index=232 label="C_methyl">]
[<Entry index=60 label="C_methane">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=42 label="CO_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=60 label="C_methane">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=7 label="O_pri">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=181 label="OOCH3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=232 label="C_methyl">]
[<Entry index=73 label="C/H3/O">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=11 label="H2O2">, <Entry index=181 label="OOCH3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=60 label="C_methane">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=42 label="CO_pri">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=16 label="Orad_O_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=181 label="OOCH3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=172 label="O2b">]
[<Entry index=4 label="H2">, <Entry index=239 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=172 label="O2b">]
[<Entry index=11 label="H2O2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=7 label="O_pri">, <Entry index=170 label="H_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=7 label="O_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/CO">, <Entry index=232 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=232 label="C_methyl">]
[<Entry index=72 label="C/H3/CO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=73 label="C/H3/O">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=7 label="O_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=170 label="H_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=60 label="C_methane">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=181 label="OOCH3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=454 label="O/H/OneDeC">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=7 label="O_pri">, <Entry index=212 label="Cb_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=60 label="C_methane">, <Entry index=176 label="O_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=170 label="H_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=443 label="OH_rad_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=60 label="C_methane">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=232 label="C_methyl">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=232 label="C_methyl">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=40 label="Cb_H">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=443 label="OH_rad_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=181 label="OOCH3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=170 label="H_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=172 label="O2b">]
[<Entry index=37 label="Cd/H/Ct">, <Entry index=170 label="H_rad">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=232 label="C_methyl">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=42 label="CO_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=321 label="C_rad/CdCdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=176 label="O_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=42 label="CO_pri">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=271 label="C_rad/H/OneDeO">]
[<Entry index=60 label="C_methane">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=212 label="Cb_rad">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=212 label="Cb_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=176 label="O_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=170 label="H_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=170 label="H_rad">]
[<Entry index=7 label="O_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=212 label="Cb_rad">]
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=212 label="Cb_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=7 label="O_pri">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=170 label="H_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=176 label="O_pri_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=60 label="C_methane">, <Entry index=181 label="OOCH3">]
[<Entry index=60 label="C_methane">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=170 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=60 label="C_methane">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=443 label="OH_rad_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=60 label="C_methane">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=232 label="C_methyl">]
[<Entry index=16 label="Orad_O_H">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=73 label="C/H3/O">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=181 label="OOCH3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=42 label="CO_pri">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=443 label="OH_rad_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=170 label="H_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/CO">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=60 label="C_methane">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=176 label="O_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=73 label="C/H3/O">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=60 label="C_methane">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=232 label="C_methyl">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=182 label="O_rad/OneDe">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=181 label="OOCH3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=176 label="O_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=7 label="O_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=443 label="OH_rad_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=212 label="Cb_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=181 label="OOCH3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=232 label="C_methyl">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=170 label="H_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=4 label="H2">, <Entry index=236 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=4 label="H2">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=172 label="O2b">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=40 label="Cb_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=443 label="OH_rad_H">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=270 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=72 label="C/H3/CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=232 label="C_methyl">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=16 label="Orad_O_H">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=73 label="C/H3/O">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=212 label="Cb_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=170 label="H_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=11 label="H2O2">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=81 label="C/H2/O2">, <Entry index=232 label="C_methyl">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=212 label="Cb_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=172 label="O2b">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=172 label="O2b">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=16 label="Orad_O_H">, <Entry index=181 label="OOCH3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=42 label="CO_pri">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=212 label="Cb_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=232 label="C_methyl">]
[<Entry index=12 label="ROOH_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=209 label="Cd_rad/Ct">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/CO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=181 label="OOCH3">]
[<Entry index=73 label="C/H3/O">, <Entry index=172 label="O2b">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=209 label="Cd_rad/Ct">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=60 label="C_methane">, <Entry index=212 label="Cb_rad">]
[<Entry index=11 label="H2O2">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=212 label="Cb_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=42 label="CO_pri">, <Entry index=181 label="OOCH3">]
[<Entry index=73 label="C/H3/O">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=73 label="C/H3/O">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=232 label="C_methyl">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=232 label="C_methyl">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=232 label="C_methyl">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=170 label="H_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/CO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=232 label="C_methyl">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=4 label="H2">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=72 label="C/H3/CO">, <Entry index=170 label="H_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=181 label="OOCH3">]
[<Entry index=93 label="C/H2/OneDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=60 label="C_methane">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=170 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=176 label="O_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=181 label="OOCH3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=60 label="C_methane">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=214 label="CO_pri_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 170,
    label = "H_rad",
    group = 
"""
1 *3 H 1
""",
    distances = DistanceData(
        distances = {'d12': -0.040336, 'd13': -0.371515, 'd23': -0.334139},
        uncertainties = {'d12': 0.109605, 'd13': 0.112044, 'd23': 0.154567},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 64 distances.
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=170 label="H_rad">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=170 label="H_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=170 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=170 label="H_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=170 label="H_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=170 label="H_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=170 label="H_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=170 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=170 label="H_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=170 label="H_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=170 label="H_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=170 label="H_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=170 label="H_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=170 label="H_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=170 label="H_rad">]
[<Entry index=37 label="Cd/H/Ct">, <Entry index=170 label="H_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=60 label="C_methane">, <Entry index=170 label="H_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=170 label="H_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=170 label="H_rad">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=170 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=170 label="H_rad">]
[<Entry index=119 label="C/H/Cs2O">, <Entry index=170 label="H_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=170 label="H_rad">]
[<Entry index=7 label="O_pri">, <Entry index=170 label="H_rad">]
[<Entry index=454 label="O/H/OneDeC">, <Entry index=170 label="H_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 434,
    label = "N3_rad",
    group = 
"""
1 *3 {N3s,N3d} 1
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 435,
    label = "N3s_rad",
    group = 
"""
1 *3 N3s 1
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 436,
    label = "NH2_rad",
    group = 
"""
1 *3 N3s 1 {2,S} {3,S}
2    H   0 {1,S}
3    H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 437,
    label = "N3s_rad_pri",
    group = 
"""
1 *3 N3s 1 {2,S} {3,S}
2    H   0 {1,S}
3    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 438,
    label = "N3s_rad_sec",
    group = 
"""
1 *3 N3s 1 {2,S} {3,S}
2    R!H 0 {1,S}
3    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 439,
    label = "N3d_rad",
    group = 
"""
1 *3 N3d 1 {2,D}
2    R!H 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 462,
    label = "N3d_rad/OneDe",
    group = 
"""
1 *3 N3d 1 {2,D}
2    Cd  0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 463,
    label = "N3d_rad/OneDeC",
    group = 
"""
1 *3 N3d 1 {2,D}
2    Cd  0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 464,
    label = "N3d_rad/OneDeCdd-O",
    group = 
"""
1 *3 N3d 1 {2,D}
2    Cd  0 {1,D} {3,D}
3    Od  0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 440,
    label = "N5_rad",
    group = 
"""
1 *3 {N5s,N5d,N5t} 1
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 441,
    label = "N5d_rad",
    group = 
"""
1 *3 N5d 1
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 171,
    label = "Y_2centeradjbirad",
    group = 
"""
1 *3 {Ct,Os,Ss} 1 {2,{S,T}}
2    {Ct,Os,Ss} 1 {1,{S,T}}
""",
    distances = DistanceData(
        distances = {'d12': 0.197008, 'd13': -0.051267, 'd23': -0.245317},
        uncertainties = {'d12': 0.184597, 'd13': 0.128513, 'd23': 0.094682},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 18 distances.
[<Entry index=10 label="O/H/NonDeO">, <Entry index=172 label="O2b">]
[<Entry index=12 label="ROOH_pri">, <Entry index=172 label="O2b">]
[<Entry index=42 label="CO_pri">, <Entry index=172 label="O2b">]
[<Entry index=73 label="C/H3/O">, <Entry index=172 label="O2b">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=172 label="O2b">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=172 label="O2b">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=172 label="O2b">]
[<Entry index=13 label="ROOH_sec">, <Entry index=172 label="O2b">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=172 label="O2b">]
[<Entry index=72 label="C/H3/CO">, <Entry index=172 label="O2b">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=172 label="O2b">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=172 label="O2b">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=172 label="O2b">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 172,
    label = "O2b",
    group = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.197008, 'd13': -0.051267, 'd23': -0.245317},
        uncertainties = {'d12': 0.184597, 'd13': 0.128513, 'd23': 0.094682},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 18 distances.
[<Entry index=10 label="O/H/NonDeO">, <Entry index=172 label="O2b">]
[<Entry index=12 label="ROOH_pri">, <Entry index=172 label="O2b">]
[<Entry index=42 label="CO_pri">, <Entry index=172 label="O2b">]
[<Entry index=73 label="C/H3/O">, <Entry index=172 label="O2b">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=172 label="O2b">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=172 label="O2b">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=172 label="O2b">]
[<Entry index=13 label="ROOH_sec">, <Entry index=172 label="O2b">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=172 label="O2b">]
[<Entry index=72 label="C/H3/CO">, <Entry index=172 label="O2b">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=172 label="O2b">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=172 label="O2b">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=172 label="O2b">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 173,
    label = "C2b",
    group = 
"""
1 *3 C 1 {2,T}
2    C 1 {1,T}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 174,
    label = "Ct_rad",
    group = 
"""
1 *3 C     1 {2,T}
2    {C,N} 0 {1,T}
""",
    distances = DistanceData(
        distances = {'d12': -0.200106, 'd13': 0.155031, 'd23': 0.41275},
        uncertainties = {'d12': 0.226116, 'd13': 0.296572, 'd23': 0.301994},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 6 distances.
[<Entry index=62 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 423,
    label = "Ct_rad/Ct",
    group = 
"""
1 *3 Ct 1 {2,T}
2    Ct 0 {1,T}
""",
    distances = DistanceData(
        distances = {'d12': -0.200106, 'd13': 0.155031, 'd23': 0.41275},
        uncertainties = {'d12': 0.226116, 'd13': 0.296572, 'd23': 0.301994},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 6 distances.
[<Entry index=62 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 424,
    label = "Ct_rad/N",
    group = 
"""
1 *3 Ct        1 {2,T}
2    {N3t,N5t} 0 {1,T}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 175,
    label = "O_rad",
    group = 
"""
1 *3 O 1 {2,S}
2    R 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.044831, 'd13': -0.144182, 'd23': -0.094245},
        uncertainties = {'d12': 0.105319, 'd13': 0.082115, 'd23': 0.106358},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 171 distances.
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=176 label="O_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=11 label="H2O2">, <Entry index=181 label="OOCH3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=40 label="Cb_H">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=60 label="C_methane">, <Entry index=181 label="OOCH3">]
[<Entry index=42 label="CO_pri">, <Entry index=181 label="OOCH3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=181 label="OOCH3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=60 label="C_methane">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=181 label="OOCH3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=176 label="O_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=176 label="O_pri_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=181 label="OOCH3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=181 label="OOCH3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=181 label="OOCH3">]
[<Entry index=42 label="CO_pri">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=73 label="C/H3/O">, <Entry index=181 label="OOCH3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=181 label="OOCH3">]
[<Entry index=11 label="H2O2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=176 label="O_pri_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=176 label="O_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=176 label="O_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=181 label="OOCH3">]
[<Entry index=60 label="C_methane">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=181 label="OOCH3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=42 label="CO_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=181 label="OOCH3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=181 label="OOCH3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=181 label="OOCH3">]
[<Entry index=4 label="H2">, <Entry index=182 label="O_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=181 label="OOCH3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=181 label="OOCH3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/CO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=181 label="OOCH3">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=181 label="OOCH3">]
[<Entry index=40 label="Cb_H">, <Entry index=181 label="OOCH3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=181 label="OOCH3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=176 label="O_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=73 label="C/H3/O">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=60 label="C_methane">, <Entry index=176 label="O_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=181 label="OOCH3">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 176,
    label = "O_pri_rad",
    group = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.196939, 'd13': -0.133898, 'd23': 0.09413},
        uncertainties = {'d12': 0.068287, 'd13': 0.156543, 'd23': 0.168874},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 13 distances.
[<Entry index=62 label="C/H3/Cs">, <Entry index=176 label="O_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=176 label="O_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=176 label="O_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=176 label="O_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=176 label="O_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=176 label="O_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=176 label="O_pri_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=176 label="O_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=176 label="O_pri_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 177,
    label = "O_sec_rad",
    group = 
"""
1 *3 O   1 {2,S}
2    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.032625, 'd13': -0.145007, 'd23': -0.109362},
        uncertainties = {'d12': 0.108314, 'd13': 0.075964, 'd23': 0.102332},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 158 distances.
[<Entry index=44 label="CO/H/NonDe">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=11 label="H2O2">, <Entry index=181 label="OOCH3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=40 label="Cb_H">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=181 label="OOCH3">]
[<Entry index=42 label="CO_pri">, <Entry index=181 label="OOCH3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=181 label="OOCH3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=60 label="C_methane">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=181 label="OOCH3">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=181 label="OOCH3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=181 label="OOCH3">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=181 label="OOCH3">]
[<Entry index=42 label="CO_pri">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=73 label="C/H3/O">, <Entry index=181 label="OOCH3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=181 label="OOCH3">]
[<Entry index=11 label="H2O2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=60 label="C_methane">, <Entry index=181 label="OOCH3">]
[<Entry index=60 label="C_methane">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=181 label="OOCH3">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=42 label="CO_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=181 label="OOCH3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=181 label="OOCH3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=181 label="OOCH3">]
[<Entry index=4 label="H2">, <Entry index=182 label="O_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=181 label="OOCH3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=181 label="OOCH3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/CO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=181 label="OOCH3">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=181 label="OOCH3">]
[<Entry index=40 label="Cb_H">, <Entry index=181 label="OOCH3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=181 label="OOCH3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=73 label="C/H3/O">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=7 label="O_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=181 label="OOCH3">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 178,
    label = "O_rad/NonDeC",
    group = 
"""
1 *3 O  1 {2,S}
2    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.097066, 'd13': -0.154804, 'd23': -0.052553},
        uncertainties = {'d12': 0.0523, 'd13': 0.072804, 'd23': 0.076912},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 44 distances.
[<Entry index=62 label="C/H3/Cs">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=60 label="C_methane">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=42 label="CO_pri">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/CO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=178 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=178 label="O_rad/NonDeC">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 179,
    label = "InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3",
    group = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {5,S} {9,S}
3     C 0 {2,S} {4,S} {10,S} {11,S}
4  *3 O 1 {3,S}
5     C 0 {2,S} {12,S} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {5,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 180,
    label = "O_rad/NonDeO",
    group = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.007343, 'd13': -0.140054, 'd23': -0.130525},
        uncertainties = {'d12': 0.117665, 'd13': 0.063588, 'd23': 0.112024},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 113 distances.
[<Entry index=44 label="CO/H/NonDe">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=11 label="H2O2">, <Entry index=181 label="OOCH3">]
[<Entry index=40 label="Cb_H">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=181 label="OOCH3">]
[<Entry index=42 label="CO_pri">, <Entry index=181 label="OOCH3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=181 label="OOCH3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=181 label="OOCH3">]
[<Entry index=60 label="C_methane">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=181 label="OOCH3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=181 label="OOCH3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=181 label="OOCH3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=181 label="OOCH3">]
[<Entry index=42 label="CO_pri">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=73 label="C/H3/O">, <Entry index=181 label="OOCH3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=181 label="OOCH3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=7 label="O_pri">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=60 label="C_methane">, <Entry index=181 label="OOCH3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=181 label="OOCH3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=181 label="OOCH3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=181 label="OOCH3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=181 label="OOCH3">]
[<Entry index=4 label="H2">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=181 label="OOCH3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=181 label="OOCH3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=181 label="OOCH3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=181 label="OOCH3">]
[<Entry index=40 label="Cb_H">, <Entry index=181 label="OOCH3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=181 label="OOCH3">]
[<Entry index=73 label="C/H3/O">, <Entry index=180 label="O_rad/NonDeO">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=180 label="O_rad/NonDeO">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 181,
    label = "OOCH3",
    group = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S} {3,S}
3    C 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.01952, 'd13': -0.139885, 'd23': -0.118261},
        uncertainties = {'d12': 0.11631, 'd13': 0.063793, 'd23': 0.123022},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 82 distances.
[<Entry index=11 label="H2O2">, <Entry index=181 label="OOCH3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=181 label="OOCH3">]
[<Entry index=42 label="CO_pri">, <Entry index=181 label="OOCH3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=181 label="OOCH3">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=181 label="OOCH3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=181 label="OOCH3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=181 label="OOCH3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=181 label="OOCH3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=181 label="OOCH3">]
[<Entry index=73 label="C/H3/O">, <Entry index=181 label="OOCH3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=181 label="OOCH3">]
[<Entry index=60 label="C_methane">, <Entry index=181 label="OOCH3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=181 label="OOCH3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=181 label="OOCH3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=181 label="OOCH3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=181 label="OOCH3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=181 label="OOCH3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=181 label="OOCH3">]
[<Entry index=4 label="H2">, <Entry index=181 label="OOCH3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=181 label="OOCH3">]
[<Entry index=40 label="Cb_H">, <Entry index=181 label="OOCH3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=181 label="OOCH3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=181 label="OOCH3">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 425,
    label = "O_rad/NonDeN",
    group = 
"""
1 *3 O   1 {2,S}
2    N3s 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 182,
    label = "O_rad/OneDe",
    group = 
"""
1 *3 O                        1 {2,S}
2    {Cd,Ct,Cb,CO,CS,N3d,N5d} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.134046, 'd13': -0.376043, 'd23': -0.238299},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=182 label="O_rad/OneDe">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 426,
    label = "O_rad/OneDeN",
    group = 
"""
1 *3 O         1 {2,S}
2    {N3d,N5d} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 403,
    label = "InChI=1S/NO3/c2-1(3)4",
    group = 
"""
1 *3 Os  1 {2,S}
2    N5d 0 {1,S} {3,D} {4,S}
3    Od  0 {2,D}
4    Os  0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 183,
    label = "InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3",
    group = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S} {4,D}
4    C 0 {3,D} {5,S}
5 *3 O 1 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 184,
    label = "InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/o",
    group = 
"""
1    C 0 {2,S} {5,S} {6,S} {7,S}
2    C 0 {1,S} {3,D} {8,S}
3    C 0 {2,D} {4,S} {9,S}
4 *3 O 1 {3,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {1,S}
8    H 0 {2,S}
9    H 0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 185,
    label = "S_rad",
    group = 
"""
1 *3 S 1 {2,S}
2    R 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 186,
    label = "S_pri_rad",
    group = 
"""
1 *3 S 1 {2,S}
2    H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 187,
    label = "S_sec_rad",
    group = 
"""
1 *3 S   1 {2,S}
2    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 188,
    label = "S_rad/NonDeC",
    group = 
"""
1 *3 S  1 {2,S}
2    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 189,
    label = "S_rad/NonDeS",
    group = 
"""
1 *3 S 1 {2,S}
2    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 190,
    label = "S_rad/OneDe",
    group = 
"""
1 *3 S                1 {2,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 191,
    label = "S_rad/Cd",
    group = 
"""
1 *3 S  1 {2,S}
2    Cd 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 192,
    label = "S_rad/CS",
    group = 
"""
1 *3 S  1 {2,S}
2    Cd 0 {1,S} {3,D}
3    S  0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 193,
    label = "S_rad/Ct",
    group = 
"""
1 *3 S  1 {2,S}
2    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 194,
    label = "S_rad/Cb",
    group = 
"""
1 *3 S  1 {2,S}
2    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 195,
    label = "S_rad/CO",
    group = 
"""
1 *3 S  1 {2,S}
2    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 196,
    label = "Cd_rad",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    R 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.073417, 'd13': 0.011981, 'd23': 0.084666},
        uncertainties = {'d12': 0.107703, 'd13': 0.09266, 'd23': 0.126892},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 148 distances.
[<Entry index=4 label="H2">, <Entry index=203 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=73 label="C/H3/O">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=209 label="Cd_rad/Ct">]
[<Entry index=60 label="C_methane">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=73 label="C/H3/O">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=37 label="Cd/H/Ct">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=209 label="Cd_rad/Ct">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=4 label="H2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=207 label="Cd_rad/Cd">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 197,
    label = "Cd_pri_rad",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.068352, 'd13': 0.014007, 'd23': 0.081995},
        uncertainties = {'d12': 0.10304, 'd13': 0.078923, 'd23': 0.125675},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 125 distances.
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=37 label="Cd/H/Ct">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=73 label="C/H3/O">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=443 label="OH_rad_H">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=73 label="C/H3/O">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=197 label="Cd_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=197 label="Cd_pri_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 198,
    label = "InChI=1/C2H3/c1-2/h1H,2H2",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D} {4,S} {5,S}
3    H 0 {1,S}
4    H 0 {2,S}
5    H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.098883, 'd13': 0.024352, 'd23': 0.119755},
        uncertainties = {'d12': 0.057973, 'd13': 0.075012, 'd23': 0.071904},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 27 distances.
[<Entry index=70 label="C/H3/Ct">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=42 label="CO_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=7 label="O_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=4 label="H2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=73 label="C/H3/O">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=60 label="C_methane">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="InChI=1/C2H3/c1-2/h1H,2H2">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 199,
    label = "InChI=1/C4H7/c1-3-4-2/h1,3H,4H2,2H3",
    group = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2     C 0 {1,S} {3,S} {8,S} {9,S}
3     C 0 {2,S} {4,D} {10,S}
4  *3 C 1 {3,D} {11,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 200,
    label = "Cd_sec_rad",
    group = 
"""
1 *3 C   1 {2,D} {3,S}
2    C   0 {1,D}
3    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.104252, 'd13': -0.000355, 'd23': 0.100921},
        uncertainties = {'d12': 0.140206, 'd13': 0.156955, 'd23': 0.144038},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 23 distances.
[<Entry index=4 label="H2">, <Entry index=203 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=4 label="H2">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=7 label="O_pri">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=209 label="Cd_rad/Ct">]
[<Entry index=4 label="H2">, <Entry index=209 label="Cd_rad/Ct">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=40 label="Cb_H">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=207 label="Cd_rad/Cd">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 201,
    label = "Cd_rad/NonDeC",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.189442, 'd13': -0.055399, 'd23': 0.130551},
        uncertainties = {'d12': 0.434881, 'd13': 0.478918, 'd23': 0.066676},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 4 distances.
[<Entry index=4 label="H2">, <Entry index=203 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 202,
    label = "InChI=1/C3H5/c1-3-2/h1H2,2H3",
    group = 
"""
1    C 0 {2,D} {4,S} {5,S}
2 *3 C 1 {1,D} {3,S}
3    C 0 {2,S} {6,S} {7,S} {8,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {3,S}
7    H 0 {3,S}
8    H 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.156314, 'd13': -0.014573, 'd23': 0.138249},
        uncertainties = {'d12': 0.268781, 'd13': 0.256596, 'd23': 0.066115},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=202 label="InChI=1/C3H5/c1-3-2/h1H2,2H3">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 203,
    label = "InChI=1/C4H7/c1-3-4-2/h3H,1-2H3",
    group = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2  *3 C 1 {1,S} {3,D}
3     C 0 {2,D} {4,S} {8,S}
4     C 0 {3,S} {9,S} {10,S} {11,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
11    H 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.332997, 'd13': -0.232311, 'd23': 0.09719},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=203 label="InChI=1/C4H7/c1-3-4-2/h3H,1-2H3">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 204,
    label = "Cd_rad/NonDeO",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    O 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 205,
    label = "Cd_rad/NonDeS",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 427,
    label = "Cd_rad/NonDeN",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    C 0 {1,D}
3    N 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 206,
    label = "Cd_rad/OneDe",
    group = 
"""
1 *3 C                1 {2,D} {3,S}
2    C                0 {1,D}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.088585, 'd13': 0.009768, 'd23': 0.095471},
        uncertainties = {'d12': 0.104498, 'd13': 0.119332, 'd23': 0.160313},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 19 distances.
[<Entry index=4 label="H2">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=7 label="O_pri">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=209 label="Cd_rad/Ct">]
[<Entry index=4 label="H2">, <Entry index=209 label="Cd_rad/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=207 label="Cd_rad/Cd">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 207,
    label = "Cd_rad/Cd",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cd 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.096765, 'd13': 0.022271, 'd23': 0.115993},
        uncertainties = {'d12': 0.111626, 'd13': 0.122649, 'd23': 0.175984},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 16 distances.
[<Entry index=4 label="H2">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=7 label="O_pri">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=207 label="Cd_rad/Cd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=207 label="Cd_rad/Cd">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 208,
    label = "Cd_rad/CS",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cd 0 {1,S} {4,D}
4    S  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 209,
    label = "Cd_rad/Ct",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Ct 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.042024, 'd13': -0.0614, 'd23': -0.021345},
        uncertainties = {'d12': 0.177176, 'd13': 0.278931, 'd23': 0.153663},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=4 label="H2">, <Entry index=209 label="Cd_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=209 label="Cd_rad/Ct">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 210,
    label = "Cd_rad/Cb",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 211,
    label = "Cd_rad/CO",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    C  0 {1,D}
3    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 212,
    label = "Cb_rad",
    group = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    distances = DistanceData(
        distances = {'d12': -0.088199, 'd13': 0.030597, 'd23': 0.119483},
        uncertainties = {'d12': 0.085584, 'd13': 0.093378, 'd23': 0.108331},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 29 distances.
[<Entry index=60 label="C_methane">, <Entry index=212 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=212 label="Cb_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=212 label="Cb_rad">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=212 label="Cb_rad">]
[<Entry index=11 label="H2O2">, <Entry index=212 label="Cb_rad">]
[<Entry index=4 label="H2">, <Entry index=212 label="Cb_rad">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=212 label="Cb_rad">]
[<Entry index=7 label="O_pri">, <Entry index=212 label="Cb_rad">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=212 label="Cb_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=212 label="Cb_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=212 label="Cb_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=212 label="Cb_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=212 label="Cb_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=212 label="Cb_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=212 label="Cb_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=212 label="Cb_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=212 label="Cb_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 213,
    label = "CO_rad",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    R 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.049238, 'd13': 0.059155, 'd23': 0.010905},
        uncertainties = {'d12': 0.081099, 'd13': 0.048564, 'd23': 0.055312},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 129 distances.
[<Entry index=90 label="C/H2/COCs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/CO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=42 label="CO_pri">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=73 label="C/H3/O">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=72 label="C/H3/CO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=16 label="Orad_O_H">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/CO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=4 label="H2">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=60 label="C_methane">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=214 label="CO_pri_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 214,
    label = "CO_pri_rad",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.038213, 'd13': 0.051218, 'd23': 0.012548},
        uncertainties = {'d12': 0.078053, 'd13': 0.045312, 'd23': 0.057795},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 41 distances.
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=60 label="C_methane">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=72 label="C/H3/CO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=73 label="C/H3/O">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=214 label="CO_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=214 label="CO_pri_rad">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 215,
    label = "CO_sec_rad",
    group = 
"""
1 *3 C   1 {2,D} {3,S}
2    O   0 {1,D}
3    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.054449, 'd13': 0.062907, 'd23': 0.010129},
        uncertainties = {'d12': 0.083995, 'd13': 0.050876, 'd23': 0.055287},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 88 distances.
[<Entry index=4 label="H2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/CO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=42 label="CO_pri">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=42 label="CO_pri">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=73 label="C/H3/O">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=60 label="C_methane">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=73 label="C/H3/O">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=60 label="C_methane">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/CO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=217 label="CO_rad/OneDe">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 216,
    label = "CO_rad/NonDe",
    group = 
"""
1 *3 C        1 {2,D} {3,S}
2    O        0 {1,D}
3    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.064743, 'd13': 0.066693, 'd23': 0.002272},
        uncertainties = {'d12': 0.098107, 'd13': 0.056449, 'd23': 0.054541},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 54 distances.
[<Entry index=4 label="H2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=42 label="CO_pri">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=73 label="C/H3/O">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=60 label="C_methane">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/CO">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=216 label="CO_rad/NonDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=216 label="CO_rad/NonDe">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 217,
    label = "CO_rad/OneDe",
    group = 
"""
1 *3 C                1 {2,D} {3,S}
2    O                0 {1,D}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.039222, 'd13': 0.057305, 'd23': 0.021751},
        uncertainties = {'d12': 0.059862, 'd13': 0.043406, 'd23': 0.059394},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 34 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=72 label="C/H3/CO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=42 label="CO_pri">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=73 label="C/H3/O">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=60 label="C_methane">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=217 label="CO_rad/OneDe">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=217 label="CO_rad/OneDe">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 218,
    label = "CS_rad",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    S 0 {1,D}
3    R 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 219,
    label = "CS_pri_rad",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    S 0 {1,D}
3    H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 220,
    label = "CS_sec_rad",
    group = 
"""
1 *3 C   1 {2,D} {3,S}
2    S   0 {1,D}
3    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 221,
    label = "CS_rad/NonDe",
    group = 
"""
1 *3 C        1 {2,D} {3,S}
2    S        0 {1,D}
3    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 222,
    label = "CS_rad/Cs",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    S  0 {1,D}
3    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 223,
    label = "CS_rad/O",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    S 0 {1,D}
3    O 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 224,
    label = "CS_rad/S",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    S 0 {1,D}
3    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 225,
    label = "CS_rad/OneDe",
    group = 
"""
1 *3 C                1 {2,D} {3,S}
2    S                0 {1,D}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 226,
    label = "CS_rad/Cd",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    S  0 {1,D}
3    Cd 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 227,
    label = "CS_rad/CS",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    S  0 {1,D}
3    Cd 0 {1,S} {4,D}
4    S  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 228,
    label = "CS_rad/Ct",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    S  0 {1,D}
3    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 229,
    label = "CS_rad/Cb",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    S  0 {1,D}
3    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 230,
    label = "CS_rad/CO",
    group = 
"""
1 *3 C  1 {2,D} {3,S}
2    S  0 {1,D}
3    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 231,
    label = "Cs_rad",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    R 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.017983, 'd13': 0.036711, 'd23': 0.017796},
        uncertainties = {'d12': 0.065503, 'd13': 0.053374, 'd23': 0.053147},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1036 distances.
[<Entry index=44 label="CO/H/NonDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=145 label="C/H/CdCd">, <Entry index=232 label="C_methyl">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=7 label="O_pri">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=45 label="InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3">, <Entry index=232 label="C_methyl">]
[<Entry index=12 label="ROOH_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=271 label="C_rad/H/OneDeO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=4 label="H2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=11 label="H2O2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=296 label="C_rad/Cs2O">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=232 label="C_methyl">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=60 label="C_methane">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=73 label="C/H3/O">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=45 label="InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=14 label="ROOH_ter">, <Entry index=232 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=60 label="C_methane">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=60 label="C_methane">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=232 label="C_methyl">]
[<Entry index=73 label="C/H3/O">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=60 label="C_methane">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=239 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/CO">, <Entry index=232 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=232 label="C_methyl">]
[<Entry index=72 label="C/H3/CO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=73 label="C/H3/O">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=42 label="CO_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=60 label="C_methane">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=42 label="CO_pri">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=443 label="OH_rad_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=4 label="H2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=60 label="C_methane">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=232 label="C_methyl">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=232 label="C_methyl">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=73 label="C/H3/O">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=232 label="C_methyl">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=73 label="C/H3/O">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=42 label="CO_pri">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=60 label="C_methane">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=40 label="Cb_H">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=40 label="Cb_H">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=7 label="O_pri">, <Entry index=232 label="C_methyl">]
[<Entry index=72 label="C/H3/CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=60 label="C_methane">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=443 label="OH_rad_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=232 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=232 label="C_methyl">]
[<Entry index=16 label="Orad_O_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/CO">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=60 label="C_methane">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=232 label="C_methyl">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=4 label="H2">, <Entry index=236 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=7 label="O_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=40 label="Cb_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=60 label="C_methane">, <Entry index=321 label="C_rad/CdCdCs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=270 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=72 label="C/H3/CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=232 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=73 label="C/H3/O">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=11 label="H2O2">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=81 label="C/H2/O2">, <Entry index=232 label="C_methyl">]
[<Entry index=12 label="ROOH_pri">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=42 label="CO_pri">, <Entry index=232 label="C_methyl">]
[<Entry index=12 label="ROOH_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=11 label="H2O2">, <Entry index=232 label="C_methyl">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=60 label="C_methane">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=73 label="C/H3/O">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=232 label="C_methyl">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=232 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=232 label="C_methyl">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=232 label="C_methyl">]
[<Entry index=42 label="CO_pri">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=232 label="C_methyl">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=4 label="H2">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=93 label="C/H2/OneDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=60 label="C_methane">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 232,
    label = "C_methyl",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.054695, 'd13': 0.032918, 'd23': 0.083781},
        uncertainties = {'d12': 0.04304, 'd13': 0.036863, 'd23': 0.061523},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 69 distances.
[<Entry index=35 label="Cd/H/Cd">, <Entry index=232 label="C_methyl">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=232 label="C_methyl">]
[<Entry index=45 label="InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3">, <Entry index=232 label="C_methyl">]
[<Entry index=7 label="O_pri">, <Entry index=232 label="C_methyl">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=232 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=232 label="C_methyl">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=145 label="C/H/CdCd">, <Entry index=232 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=232 label="C_methyl">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=232 label="C_methyl">]
[<Entry index=443 label="OH_rad_H">, <Entry index=232 label="C_methyl">]
[<Entry index=68 label="InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3">, <Entry index=232 label="C_methyl">]
[<Entry index=42 label="CO_pri">, <Entry index=232 label="C_methyl">]
[<Entry index=14 label="ROOH_ter">, <Entry index=232 label="C_methyl">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=232 label="C_methyl">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=232 label="C_methyl">]
[<Entry index=73 label="C/H3/O">, <Entry index=232 label="C_methyl">]
[<Entry index=81 label="C/H2/O2">, <Entry index=232 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=232 label="C_methyl">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=232 label="C_methyl">]
[<Entry index=72 label="C/H3/CO">, <Entry index=232 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=232 label="C_methyl">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=232 label="C_methyl">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=232 label="C_methyl">]
[<Entry index=40 label="Cb_H">, <Entry index=232 label="C_methyl">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=232 label="C_methyl">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=232 label="C_methyl">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=232 label="C_methyl">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 233,
    label = "C_pri_rad",
    group = 
"""
1 *3 C   1 {2,S} {3,S} {4,S}
2    H   0 {1,S}
3    H   0 {1,S}
4    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.006918, 'd13': 0.029209, 'd23': 0.034731},
        uncertainties = {'d12': 0.058883, 'd13': 0.048769, 'd23': 0.051727},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 543 distances.
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=239 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=11 label="H2O2">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=4 label="H2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=73 label="C/H3/O">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=45 label="InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=16 label="Orad_O_H">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=7 label="O_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=11 label="H2O2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=7 label="O_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=60 label="C_methane">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=73 label="C/H3/O">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=60 label="C_methane">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=60 label="C_methane">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/CO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=60 label="C_methane">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=42 label="CO_pri">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=443 label="OH_rad_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=60 label="C_methane">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=4 label="H2">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=93 label="C/H2/OneDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=4 label="H2">, <Entry index=236 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=60 label="C_methane">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=60 label="C_methane">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=72 label="C/H3/CO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=73 label="C/H3/O">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=72 label="C/H3/CO">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=247 label="C_rad/H2/O">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 234,
    label = "C_rad/H2/Cs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.037988, 'd13': 0.025699, 'd23': 0.060809},
        uncertainties = {'d12': 0.060435, 'd13': 0.055424, 'd23': 0.048674},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 277 distances.
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=236 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=42 label="CO_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=60 label="C_methane">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=60 label="C_methane">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=93 label="C/H2/OneDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=239 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=7 label="O_pri">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=42 label="CO_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=11 label="H2O2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=40 label="Cb_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=7 label="O_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=45 label="InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=234 label="C_rad/H2/Cs">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 235,
    label = "InChI=1/C2H5/c1-2/h1H2,2H3",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    C 0 {1,S} {5,S} {6,S} {7,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
7    H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.029017, 'd13': 0.031706, 'd23': 0.05723},
        uncertainties = {'d12': 0.052433, 'd13': 0.036586, 'd23': 0.058155},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 57 distances.
[<Entry index=81 label="C/H2/O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=60 label="C_methane">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=4 label="H2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=76 label="C/H2/NonDeC">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=11 label="H2O2">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=93 label="C/H2/OneDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=42 label="CO_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=40 label="Cb_H">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=7 label="O_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=235 label="InChI=1/C2H5/c1-2/h1H2,2H3">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 236,
    label = "InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2",
    group = 
"""
1  *3 C 1 {2,S} {6,S} {7,S}
2     C 0 {1,S} {3,S} {8,S} {9,S}
3     C 0 {2,S} {4,S} {10,S} {11,S}
4     C 0 {3,S} {5,S} {12,S} {13,S}
5     O 0 {4,S} {14,S}
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
    distances = DistanceData(
        distances = {'d12': -0.29106, 'd13': -0.249295, 'd23': 0.038366},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=236 label="InChI=1/C4H9O/c1-2-3-4-5/h5H,1-4H2">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 237,
    label = "InChI=1/C4H9O/c1-3-4(2)5/h4-5H,2-3H2,1H3",
    group = 
"""
1     C 0 {3,S} {6,S} {7,S} {8,S}
2  *3 C 1 {4,S} {9,S} {10,S}
3     C 0 {1,S} {4,S} {11,S} {12,S}
4     C 0 {2,S} {3,S} {5,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 238,
    label = "InChI=1/C4H9O/c1-3-4(2)5/h4-5H,1,3H2,2H3",
    group = 
"""
1  *3 C 1 {3,S} {6,S} {7,S}
2     C 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 {1,S} {4,S} {11,S} {12,S}
4     C 0 {2,S} {3,S} {5,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 239,
    label = "InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3",
    group = 
"""
1  *3 C 1 {4,S} {6,S} {7,S}
2     C 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 {4,S} {11,S} {12,S} {13,S}
4     C 0 {1,S} {2,S} {3,S} {5,S}
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
    distances = DistanceData(
        distances = {'d12': -0.297145, 'd13': -0.243606, 'd23': 0.049827},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=239 label="InChI=1/C4H9O/c1-4(2,3)5/h5H,1H2,2-3H3">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 240,
    label = "InChI=1/C4H9O/c1-4(2)3-5/h4-5H,1,3H2,2H3",
    group = 
"""
1  *3 C 1 {2,S} {6,S} {7,S}
2     C 0 {1,S} {3,S} {5,S} {8,S}
3     C 0 {2,S} {4,S} {9,S} {10,S}
4     O 0 {3,S} {11,S}
5     C 0 {2,S} {12,S} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {5,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 241,
    label = "C_rad/H2/Cd",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.050239, 'd13': 0.042449, 'd23': -0.010112},
        uncertainties = {'d12': 0.06665, 'd13': 0.048158, 'd23': 0.058034},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 128 distances.
[<Entry index=79 label="C/H2/CsO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=60 label="C_methane">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=4 label="H2">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=72 label="C/H3/CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=60 label="C_methane">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=42 label="CO_pri">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=11 label="H2O2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=73 label="C/H3/O">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=73 label="C/H3/O">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=241 label="C_rad/H2/Cd">]
[<Entry index=4 label="H2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=60 label="C_methane">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="C_rad/H2/Cd">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 242,
    label = "InChI=1/C3H5/c1-3-2/h3H,1-2H2",
    group = 
"""
1 *3 C 1 {2,S} {4,S} {5,S}
2    C 0 {1,S} {3,D} {6,S}
3    C 0 {2,D}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.053069, 'd13': 0.043706, 'd23': -0.011548},
        uncertainties = {'d12': 0.072022, 'd13': 0.050271, 'd23': 0.063208},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 100 distances.
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=60 label="C_methane">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=42 label="CO_pri">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=11 label="H2O2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=40 label="Cb_H">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=73 label="C/H3/O">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
[<Entry index=4 label="H2">, <Entry index=242 label="InChI=1/C3H5/c1-3-2/h3H,1-2H2">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 243,
    label = "InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3",
    group = 
"""
1     C 0 {2,D} {5,S} {6,S}
2     C 0 {1,D} {3,S} {4,S}
3  *3 C 1 {2,S} {7,S} {8,S}
4     C 0 {2,S} {9,S} {10,S} {11,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {3,S}
8     H 0 {3,S}
9     H 0 {4,S}
10    H 0 {4,S}
11    H 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.029697, 'd13': 0.015334, 'd23': -0.018901},
        uncertainties = {'d12': 0.110837, 'd13': 0.186897, 'd23': 0.092543},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=16 label="Orad_O_H">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=60 label="C_methane">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="InChI=1/C4H7/c1-4(2)3/h1-2H2,3H3">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 244,
    label = "C_rad/H2/Ct",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.014919, 'd13': 0.027219, 'd23': 0.009122},
        uncertainties = {'d12': 0.052741, 'd13': 0.028879, 'd23': 0.049029},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 27 distances.
[<Entry index=73 label="C/H3/O">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=4 label="H2">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=72 label="C/H3/CO">, <Entry index=244 label="C_rad/H2/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=244 label="C_rad/H2/Ct">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 245,
    label = "C_rad/H2/Cb",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 246,
    label = "C_rad/H2/CO",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    CO 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.008839, 'd13': 0.019735, 'd23': 0.030685},
        uncertainties = {'d12': 0.044491, 'd13': 0.03721, 'd23': 0.058519},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 63 distances.
[<Entry index=9 label="O/H/NonDeC">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=73 label="C/H3/O">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=60 label="C_methane">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=443 label="OH_rad_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=16 label="Orad_O_H">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=246 label="C_rad/H2/CO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=246 label="C_rad/H2/CO">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 247,
    label = "C_rad/H2/O",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.001562, 'd13': 0.025899, 'd23': 0.030713},
        uncertainties = {'d12': 0.054885, 'd13': 0.034052, 'd23': 0.050786},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 48 distances.
[<Entry index=10 label="O/H/NonDeO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=443 label="OH_rad_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/CO">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=40 label="Cb_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=60 label="C_methane">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=4 label="H2">, <Entry index=247 label="C_rad/H2/O">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=247 label="C_rad/H2/O">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 248,
    label = "C_rad/H2/S",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 428,
    label = "C_rad/H2/N",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    N 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 249,
    label = "C_sec_rad",
    group = 
"""
1 *3 C   1 {2,S} {3,S} {4,S}
2    H   0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.061029, 'd13': 0.046822, 'd23': -0.014353},
        uncertainties = {'d12': 0.077421, 'd13': 0.057808, 'd23': 0.056367},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 333 distances.
[<Entry index=73 label="C/H3/O">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=60 label="C_methane">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=73 label="C/H3/O">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=16 label="Orad_O_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=271 label="C_rad/H/OneDeO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=60 label="C_methane">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=11 label="H2O2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=4 label="H2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=42 label="CO_pri">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=40 label="Cb_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=60 label="C_methane">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=60 label="C_methane">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=60 label="C_methane">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=73 label="C/H3/O">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=72 label="C/H3/CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=60 label="C_methane">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=270 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=72 label="C/H3/CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=265 label="C_rad/H/CdCs">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 250,
    label = "C_rad/H/NonDeC",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.026987, 'd13': 0.013257, 'd23': 0.036995},
        uncertainties = {'d12': 0.057045, 'd13': 0.032933, 'd23': 0.060731},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 62 distances.
[<Entry index=73 label="C/H3/O">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=11 label="H2O2">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=40 label="Cb_H">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=72 label="C/H3/CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=4 label="H2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=11 label="H2O2">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=443 label="OH_rad_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=42 label="CO_pri">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=60 label="C_methane">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=250 label="C_rad/H/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 251,
    label = "InChI=1/C3H7/c1-3-2/h3H,1-2H3",
    group = 
"""
1     C 0 {2,S} {4,S} {5,S} {6,S}
2  *3 C 1 {1,S} {3,S} {7,S}
3     C 0 {2,S} {8,S} {9,S} {10,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.019178, 'd13': 0.034976, 'd23': 0.051157},
        uncertainties = {'d12': 0.043982, 'd13': 0.032447, 'd23': 0.057282},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 42 distances.
[<Entry index=73 label="C/H3/O">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=116 label="C/H/Cs3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=4 label="H2">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=42 label="CO_pri">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=11 label="H2O2">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=251 label="InChI=1/C3H7/c1-3-2/h3H,1-2H3">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 252,
    label = "InChI=1/C4H9O/c1-2-3-4-5/h2,5H,3-4H2,1H3",
    group = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *3 C 1 {1,S} {3,S} {9,S}
3     C 0 {2,S} {4,S} {10,S} {11,S}
4     C 0 {3,S} {5,S} {12,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 253,
    label = "InChI=1/C4H9O/c1-2-3-4-5/h3,5H,2,4H2,1H3",
    group = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {9,S} {10,S}
3  *3 C 1 {2,S} {4,S} {11,S}
4     C 0 {3,S} {5,S} {12,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 254,
    label = "InChI=1/C4H9O/c1-3-4(2)5/h3-5H,1-2H3",
    group = 
"""
1     C 0 {3,S} {6,S} {7,S} {8,S}
2     C 0 {4,S} {9,S} {10,S} {11,S}
3  *3 C 1 {1,S} {4,S} {12,S}
4     C 0 {2,S} {3,S} {5,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 255,
    label = "C_rad/H/NonDeO",
    group = 
"""
1 *3 C      1 {2,S} {3,S} {4,S}
2    H      0 {1,S}
3    O      0 {1,S}
4    {Cs,O} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.013231, 'd13': 0.02952, 'd23': 0.023645},
        uncertainties = {'d12': 0.077556, 'd13': 0.043877, 'd23': 0.061036},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 43 distances.
[<Entry index=86 label="C/H2/CdCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=60 label="C_methane">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=60 label="C_methane">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=73 label="C/H3/O">, <Entry index=256 label="C_rad/H/CsO">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 256,
    label = "C_rad/H/CsO",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    O  0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.014645, 'd13': 0.0299, 'd23': 0.022958},
        uncertainties = {'d12': 0.077363, 'd13': 0.044532, 'd23': 0.061124},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 41 distances.
[<Entry index=86 label="C/H2/CdCs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=60 label="C_methane">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=11 label="H2O2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=72 label="C/H3/CO">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=73 label="C/H3/O">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=256 label="C_rad/H/CsO">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=256 label="C_rad/H/CsO">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 257,
    label = "InChI=1/C4H9O/c1-2-3-4-5/h4-5H,2-3H2,1H3",
    group = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {9,S} {10,S}
3     C 0 {2,S} {4,S} {11,S} {12,S}
4  *3 C 1 {3,S} {5,S} {13,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 258,
    label = "InChI=1/C4H9O/c1-4(2)3-5/h3-5H,1-2H3",
    group = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2     C 0 {1,S} {3,S} {5,S} {9,S}
3  *3 C 1 {2,S} {4,S} {10,S}
4     O 0 {3,S} {11,S}
5     C 0 {2,S} {12,S} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {5,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 259,
    label = "C_rad/H/O2",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    O 0 {1,S}
4    O 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.017875, 'd13': 0.021177, 'd23': 0.038742},
        uncertainties = {'d12': 0.743243, 'd13': 0.264721, 'd23': 0.54389},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=259 label="C_rad/H/O2">]
[<Entry index=60 label="C_methane">, <Entry index=259 label="C_rad/H/O2">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 260,
    label = "C_rad/H/NonDeS",
    group = 
"""
1 *3 C      1 {2,S} {3,S} {4,S}
2    H      0 {1,S}
3    S      0 {1,S}
4    {Cs,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 261,
    label = "C_rad/H/CsS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 262,
    label = "C_rad/H/S2",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    S 0 {1,S}
4    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 430,
    label = "C_rad/H/NonDeCN",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    C 0 {1,S}
4    N 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 431,
    label = "C_rad/H/NonDeON",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    O 0 {1,S}
4    N 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 432,
    label = "C_rad/H/NonDeNN",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    N 0 {1,S}
4    N 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 263,
    label = "C_rad/H/OneDe",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cs,O,S}         0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.073917, 'd13': 0.050314, 'd23': -0.024349},
        uncertainties = {'d12': 0.077303, 'd13': 0.05462, 'd23': 0.057394},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 143 distances.
[<Entry index=98 label="C/H2/CdCd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=271 label="C_rad/H/OneDeO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=270 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=60 label="C_methane">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=40 label="Cb_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=11 label="H2O2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=265 label="C_rad/H/CdCs">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 264,
    label = "C_rad/H/OneDeC",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.073529, 'd13': 0.050157, 'd23': -0.02413},
        uncertainties = {'d12': 0.077428, 'd13': 0.054785, 'd23': 0.057503},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 142 distances.
[<Entry index=98 label="C/H2/CdCd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=270 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=60 label="C_methane">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=40 label="Cb_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=11 label="H2O2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=60 label="C_methane">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=265 label="C_rad/H/CdCs">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 265,
    label = "C_rad/H/CdCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.083405, 'd13': 0.053224, 'd23': -0.03157},
        uncertainties = {'d12': 0.08231, 'd13': 0.059101, 'd23': 0.057634},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 117 distances.
[<Entry index=42 label="CO_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=60 label="C_methane">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=73 label="C/H3/O">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=69 label="InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=40 label="Cb_H">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=265 label="C_rad/H/CdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=265 label="C_rad/H/CdCs">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 266,
    label = "C_rad/H/CSCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S} {5,D}
4    Cs 0 {1,S}
5    S  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 267,
    label = "C_rad/H/CtCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 268,
    label = "C_rad/H/CbCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 269,
    label = "C_rad/H/CO/Cs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    CO 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.028186, 'd13': 0.036077, 'd23': 0.010029},
        uncertainties = {'d12': 0.05321, 'd13': 0.029788, 'd23': 0.061153},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 25 distances.
[<Entry index=98 label="C/H2/CdCd">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=73 label="C/H3/O">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=270 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
[<Entry index=60 label="C_methane">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/CO">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H/CO/Cs">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=269 label="C_rad/H/CO/Cs">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 270,
    label = "InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c",
    group = 
"""
1    C 0 {2,S} {5,S} {6,S} {7,S}
2 *3 C 1 {1,S} {3,S} {8,S}
3    C 0 {2,S} {4,D} {9,S}
4    O 0 {3,D}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {1,S}
8    H 0 {2,S}
9    H 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.093056, 'd13': 0.051855, 'd23': -0.043081},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=270 label="InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 271,
    label = "C_rad/H/OneDeO",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    O                0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.123475, 'd13': 0.070311, 'd23': -0.052237},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=271 label="C_rad/H/OneDeO">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 272,
    label = "C_rad/H/OneDeS",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    S                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 273,
    label = "C_rad/H/CdS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    S  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 274,
    label = "C_rad/H/CtS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    S  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 433,
    label = "C_rad/H/OneDeN",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    C 0 {1,S}
4    N 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 275,
    label = "C_rad/H/TwoDe",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.121383, 'd13': 0.071744, 'd23': -0.050453},
        uncertainties = {'d12': 0.093437, 'd13': 0.081734, 'd23': 0.052348},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 85 distances.
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=73 label="C/H3/O">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=40 label="Cb_H">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=60 label="C_methane">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H/CdCd">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 276,
    label = "C_rad/H/CdCd",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.121383, 'd13': 0.071744, 'd23': -0.050453},
        uncertainties = {'d12': 0.093437, 'd13': 0.081734, 'd23': 0.052348},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 85 distances.
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=70 label="C/H3/Ct">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=73 label="C/H3/O">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/CO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=40 label="Cb_H">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=60 label="C_methane">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=276 label="C_rad/H/CdCd">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H/CdCd">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 277,
    label = "C_rad/H/CdCS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 278,
    label = "C_rad/H/CSCS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S} {5,D}
4    Cd 0 {1,S} {6,D}
5    S  0 {3,D}
6    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 279,
    label = "C_rad/H/CdCt",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 280,
    label = "C_rad/H/CtCS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 281,
    label = "C_rad/H/CdCb",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 282,
    label = "C_rad/H/CbCS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 283,
    label = "C_rad/H/CdCO",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cd 0 {1,S}
4    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 284,
    label = "C_rad/H/COCS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    CO 0 {1,S}
4    Cd 0 {1,S} {5,D}
5    S  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 285,
    label = "C_rad/H/CtCt",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 286,
    label = "C_rad/H/CtCb",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 287,
    label = "C_rad/H/CtCO",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Ct 0 {1,S}
4    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 288,
    label = "C_rad/H/CbCb",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 289,
    label = "C_rad/H/CbCO",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cb 0 {1,S}
4    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 290,
    label = "C_rad/H/COCO",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    CO 0 {1,S}
4    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 291,
    label = "C_ter_rad",
    group = 
"""
1 *3 C   1 {2,S} {3,S} {4,S}
2    R!H 0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.063452, 'd13': 0.047076, 'd23': -0.015169},
        uncertainties = {'d12': 0.07267, 'd13': 0.073075, 'd23': 0.045001},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 91 distances.
[<Entry index=44 label="CO/H/NonDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=40 label="Cb_H">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=73 label="C/H3/O">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=443 label="OH_rad_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=60 label="C_methane">, <Entry index=321 label="C_rad/CdCdCs">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=296 label="C_rad/Cs2O">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=60 label="C_methane">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=7 label="O_pri">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=73 label="C/H3/O">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=4 label="H2">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=72 label="C/H3/CO">, <Entry index=311 label="C_rad/COCs2">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 292,
    label = "C_rad/NonDe",
    group = 
"""
1 *3 C        1 {2,S} {3,S} {4,S}
2    {Cs,O,S} 0 {1,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.003109, 'd13': 0.012299, 'd23': 0.007189},
        uncertainties = {'d12': 0.133667, 'd13': 0.14505, 'd23': 0.062725},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 16 distances.
[<Entry index=44 label="CO/H/NonDe">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=11 label="H2O2">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=40 label="Cb_H">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=42 label="CO_pri">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=73 label="C/H3/O">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=4 label="H2">, <Entry index=296 label="C_rad/Cs2O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=4 label="H2">, <Entry index=293 label="C_rad/Cs3">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 293,
    label = "C_rad/Cs3",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.0051, 'd13': 0.01983, 'd23': 0.012794},
        uncertainties = {'d12': 0.059505, 'd13': 0.053283, 'd23': 0.063173},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 15 distances.
[<Entry index=44 label="CO/H/NonDe">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=11 label="H2O2">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=40 label="Cb_H">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=42 label="CO_pri">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=73 label="C/H3/O">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=293 label="C_rad/Cs3">]
[<Entry index=4 label="H2">, <Entry index=293 label="C_rad/Cs3">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 294,
    label = "InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3",
    group = 
"""
1     C 0 {2,S} {6,S} {7,S} {8,S}
2  *3 C 1 {1,S} {3,S} {5,S}
3     C 0 {2,S} {4,S} {9,S} {10,S}
4     O 0 {3,S} {11,S}
5     C 0 {2,S} {12,S} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {5,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 295,
    label = "C_rad/NDMustO",
    group = 
"""
1 *3 C      1 {2,S} {3,S} {4,S}
2    O      0 {1,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.044016, 'd13': -0.165951, 'd23': -0.125477},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=296 label="C_rad/Cs2O">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 296,
    label = "C_rad/Cs2O",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    O  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.044016, 'd13': -0.165951, 'd23': -0.125477},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=296 label="C_rad/Cs2O">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 297,
    label = "C_rad/OOH/Cs/Cs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    O  0 {1,S} {5,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    O  0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 298,
    label = "InChI=1/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3",
    group = 
"""
1     C 0 {3,S} {6,S} {7,S} {8,S}
2     C 0 {4,S} {9,S} {10,S} {11,S}
3     C 0 {1,S} {4,S} {12,S} {13,S}
4  *3 C 1 {2,S} {3,S} {5,S}
5     O 0 {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {2,S}
12    H 0 {3,S}
13    H 0 {3,S}
14    H 0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 299,
    label = "C_rad/CsO2",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    O  0 {1,S}
3    O  0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 300,
    label = "C_rad/O3",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    O 0 {1,S}
3    O 0 {1,S}
4    O 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 301,
    label = "C_rad/NDMustS",
    group = 
"""
1 *3 C      1 {2,S} {3,S} {4,S}
2    S      0 {1,S}
3    {Cs,S} 0 {1,S}
4    {Cs,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 302,
    label = "C_rad/Cs2S",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 303,
    label = "C_rad/CsS2",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    S  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 304,
    label = "C_rad/S3",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    S 0 {1,S}
3    S 0 {1,S}
4    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 305,
    label = "C_rad/OneDe",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    {Cs,O,S}         0 {1,S}
4    {Cs,O,S}         0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.072926, 'd13': 0.0526, 'd23': -0.018459},
        uncertainties = {'d12': 0.056118, 'd13': 0.053224, 'd23': 0.041066},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 74 distances.
[<Entry index=44 label="CO/H/NonDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=443 label="OH_rad_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=60 label="C_methane">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=7 label="O_pri">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=73 label="C/H3/O">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=311 label="C_rad/COCs2">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 306,
    label = "C_rad/Cs2",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    Cs               0 {1,S}
4    Cs               0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.072926, 'd13': 0.0526, 'd23': -0.018459},
        uncertainties = {'d12': 0.056118, 'd13': 0.053224, 'd23': 0.041066},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 74 distances.
[<Entry index=44 label="CO/H/NonDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=443 label="OH_rad_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=60 label="C_methane">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=7 label="O_pri">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=73 label="C/H3/O">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=311 label="C_rad/COCs2">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 307,
    label = "C_rad/CdCs2",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 308,
    label = "C_rad/CSCs2",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    S  0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 309,
    label = "C_rad/CtCs2",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 310,
    label = "C_rad/CbCs2",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 311,
    label = "C_rad/COCs2",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    CO 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.072926, 'd13': 0.0526, 'd23': -0.018459},
        uncertainties = {'d12': 0.056118, 'd13': 0.053224, 'd23': 0.041066},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 74 distances.
[<Entry index=44 label="CO/H/NonDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=65 label="C/H3/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=79 label="C/H2/CsO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=134 label="C/H/Cs2CO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=443 label="OH_rad_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=67 label="InChI=1/C3H6/c1-3-2/h3H,1H2,2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=77 label="InChI=1/C3H8/c1-3-2/h3H2,1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=46 label="CO/H/OneDe">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=98 label="C/H2/CdCd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=86 label="C/H2/CdCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=63 label="InChI=1/C2H6/c1-2/h1-2H3">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=60 label="C_methane">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=90 label="C/H2/COCs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=35 label="Cd/H/Cd">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=62 label="C/H3/Cs">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=7 label="O_pri">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=73 label="C/H3/O">, <Entry index=311 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/CO">, <Entry index=311 label="C_rad/COCs2">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 312,
    label = "C_rad/CsO",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    O                0 {1,S}
4    Cs               0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 313,
    label = "C_rad/CsS",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    S                0 {1,S}
4    Cs               0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 314,
    label = "C_rad/CdCsS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 315,
    label = "C_rad/CtCsS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 316,
    label = "C_rad/O2",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    O                0 {1,S}
4    O                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 317,
    label = "C_rad/OS",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    S                0 {1,S}
4    O                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 318,
    label = "C_rad/S2",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    S                0 {1,S}
4    S                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 319,
    label = "C_rad/TwoDe",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cs,O,S}         0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.270326, 'd13': 0.160176, 'd23': -0.112938},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=60 label="C_methane">, <Entry index=321 label="C_rad/CdCdCs">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 320,
    label = "C_rad/Cs",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.270326, 'd13': 0.160176, 'd23': -0.112938},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=60 label="C_methane">, <Entry index=321 label="C_rad/CdCdCs">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 321,
    label = "C_rad/CdCdCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cd 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.270326, 'd13': 0.160176, 'd23': -0.112938},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=60 label="C_methane">, <Entry index=321 label="C_rad/CdCdCs">]
""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 322,
    label = "C_rad/CdCSCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cd 0 {1,S} {5,D}
4    Cs 0 {1,S}
5    S  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 323,
    label = "C_rad/CSCSCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S} {5,D}
3    Cd 0 {1,S} {6,D}
4    Cs 0 {1,S}
5    S  0 {2,D}
6    S  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 324,
    label = "C_rad/CdCtCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 325,
    label = "C_rad/CtCSCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cd 0 {1,S} {5,D}
4    Cs 0 {1,S}
5    S  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 326,
    label = "C_rad/CdCbCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 327,
    label = "C_rad/CbCSCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cd 0 {1,S} {5,D}
4    Cs 0 {1,S}
5    S  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 328,
    label = "C_rad/CdCOCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cd 0 {1,S}
3    CO 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 329,
    label = "C_rad/COCSCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    CO 0 {1,S}
3    Cd 0 {1,S} {5,D}
4    Cs 0 {1,S}
5    S  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 330,
    label = "C_rad/CtCtCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Ct 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 331,
    label = "C_rad/CtCbCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 332,
    label = "C_rad/CtCOCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Ct 0 {1,S}
3    CO 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 333,
    label = "C_rad/CbCbCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    Cb 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 334,
    label = "C_rad/CbCOCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cb 0 {1,S}
3    CO 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 335,
    label = "C_rad/COCOCs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    CO 0 {1,S}
3    CO 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 336,
    label = "C_rad/TDMustO",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    O                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 337,
    label = "C_rad/TDMustS",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    S                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

entry(
    index = 338,
    label = "C_rad/ThreeDe",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2014-05-26","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Copied kinetics group definitions"""),
    ],
)

tree(
"""
L1: X_H_or_Xrad_H_Xbirad_H_Xtrirad_H
    L2: X_H
        L3: H2
        L3: N3_H
            L4: N3d_H
                L5: N3d/H/NonDe
                    L6: N3d/H/NonDeO
                    L6: N3d/H/NonDeN
                    L6: N3d/H/NonDeC
                L5: N3d/H/OneDe
                    L6: N3d/H/OneDeC
                    L6: N3d/H/OneDeN
            L4: N3s_H
                L5: NH3
                L5: N3s_pri_H
                    L6: N3s/H2/NonDe
                        L7: N3s/H2/NonDeC
                        L7: N3s/H2/NonDeO
                        L7: N3s/H2/NonDeN
                    L6: N3s/H2/OneDe
                        L7: N3s/H2/OneDeN
                L5: N3s_sec_H
        L3: N5_H
            L4: N5d_H
                L5: N5d/H/NonDeOO
        L3: Ct_H
            L4: Ct/H/NonDeC
            L4: Ct/H/NonDeN
        L3: O_H
            L4: O_pri
            L4: O_sec
                L5: O/H/NonDeC
                L5: O/H/NonDeO
                    L6: H2O2
                    L6: ROOH_pri
                    L6: ROOH_sec
                    L6: ROOH_ter
                L5: O/H/NonDeN
                L5: O/H/OneDe
                    L6: O/H/OneDeC
                    L6: O/H/OneDeN
        L3: Orad_O_H
        L3: S_H
            L4: S_pri
            L4: S_sec
                L5: S/H/NonDeC
                L5: S/H/NonDeS
                L5: S/H/OneDe
                    L6: S/H/Cd
                        L7: S/H/CS
                    L6: S/H/Ct
                    L6: S/H/Cb
                    L6: S/H/CO
        L3: Cd_H
            L4: Cd_pri
                L5: Cd/H2/NonDeC
                L5: Cd/H2/NonDeN
            L4: Cd_sec
                L5: Cd/H/NonDeC
                L5: Cd/H/NonDeO
                L5: Cd/H/NonDeS
                L5: Cd/H/NonDeN
                L5: Cd/H/OneDe
                    L6: Cd/H/Cd
                        L7: Cd/H/CS
                    L6: Cd/H/Ct
                    L6: Cd/H/Cb
                    L6: Cd/H/CO
                    L6: Cd/H/N
        L3: Cb_H
        L3: CO_H
            L4: CO_pri
            L4: CO_sec
                L5: CO/H/NonDe
                    L6: InChI=1/C4H8O/c1-2-3-4-5/h4H,2-3H2,1H3
                L5: CO/H/OneDe
        L3: CS_H
            L4: CS_pri
            L4: CS_sec
                L5: CS/H/NonDeC
                L5: CS/H/NonDeO
                L5: CS/H/NonDeS
                L5: CS/H/OneDe
                    L6: CS/H/Cd
                        L7: CS/H/CS
                    L6: CS/H/Ct
                    L6: CS/H/Cb
                    L6: CS/H/CO
        L3: Cs_H
            L4: C_methane
            L4: C_pri
                L5: C/H3/Cs
                    L6: InChI=1/C2H6/c1-2/h1-2H3
                    L6: InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/gamma
                L5: C/H3/Cd
                    L6: C/H3/CS
                    L6: InChI=1/C3H6/c1-3-2/h3H,1H2,2H3
                    L6: InChI=1/C4H8/c1-4(2)3/h1H2,2-3H3
                    L6: InChI=1/C4H8/c1-3-4-2/h3-4H,1-2H3/b4-3+
                L5: C/H3/Ct
                L5: C/H3/Cb
                L5: C/H3/CO
                L5: C/H3/O
                L5: C/H3/S
                L5: Cs/H3/NonDeN
                L5: Cs/H3/OneDeN
            L4: C_sec
                L5: C/H2/NonDeC
                    L6: InChI=1/C3H8/c1-3-2/h3H2,1-2H3
                L5: C/H2/NonDeO
                    L6: C/H2/CsO
                        L7: InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/alpha
                    L6: C/H2/O2
                L5: C/H2/NonDeS
                    L6: C/H2/CsS
                L5: C/H2/NonDeN
                L5: C/H2/OneDe
                    L6: C/H2/OneDeC
                        L7: C/H2/CdCs
                            L8: C/H2/CSCs
                        L7: C/H2/CtCs
                        L7: C/H2/CbCs
                        L7: C/H2/COCs
                        L7: InChI=1/C3H6O/c1-2-3-4/h3H,2H2,1H3/beta
                        L7: InChI=1/C4H8/c1-3-4-2/h3H,1,4H2,2H3
                    L6: C/H2/OneDeO
                    L6: C/H2/OneDeS
                        L7: C/H2/CdS
                        L7: C/H2/CtS
                L5: C/H2/TwoDe
                    L6: C/H2/CdCd
                        L7: C/H2/CdCS
                        L7: C/H2/CSCS
                    L6: C/H2/CdCt
                        L7: C/H2/CtCS
                    L6: C/H2/CdCb
                        L7: C/H2/CbCS
                    L6: C/H2/CdCO
                        L7: C/H2/COCS
                    L6: C/H2/CtCt
                    L6: C/H2/CtCb
                    L6: C/H2/CtCO
                    L6: C/H2/CbCb
                    L6: C/H2/CbCO
                    L6: C/H2/COCO
                L5: C/H2/Cb
            L4: C_ter
                L5: C/H/NonDeC
                    L6: C/H/Cs3
                        L7: InChI=1/C4H10O/c1-4(2)3-5/h4-5H,3H2,1-2H3/beta
                    L6: C/H/Cs2N
                    L6: C/H/NDMustO
                        L7: C/H/Cs2O
                        L7: C/H/CsO2
                        L7: C/H/O3
                    L6: C/H/NDMustS
                        L7: C/H/Cs2S
                        L7: C/H/CsS2
                        L7: C/H/S3
                    L6: C/H/NDMustOS
                        L7: C/H/CsOS
                L5: C/H/OneDe
                    L6: C/H/Cs2
                        L7: C/H/Cs2Cd
                            L8: C/H/Cs2CS
                        L7: C/H/Cs2Ct
                        L7: C/H/Cs2Cb
                        L7: C/H/Cs2CO
                        L7: InChI=1/C4H8O/c1-4(2)3-5/h3-4H,1-2H3
                    L6: C/H/CsO
                    L6: C/H/CsS
                        L7: C/H/CdCsS
                        L7: C/H/CtCsS
                    L6: C/H/OO
                    L6: C/H/OS
                    L6: C/H/SS
                L5: C/H/TwoDe
                    L6: C/H/Cs
                        L7: C/H/CdCd
                            L8: C/H/CdCS
                            L8: C/H/CSCS
                        L7: C/H/CdCt
                            L8: C/H/CtCS
                        L7: C/H/CdCb
                            L8: C/H/CbCS
                        L7: C/H/CdCO
                            L8: C/H/COCS
                        L7: C/H/CtCt
                        L7: C/H/CtCb
                        L7: C/H/CtCO
                        L7: C/H/CbCb
                        L7: C/H/CbCO
                        L7: C/H/COCO
                    L6: C/H/TDMustO
                    L6: C/H/TDMustS
                L5: C/H/ThreeDe
                L5: C/H/Cb
    L2: Xrad_H
        L3: C_rad_H
            L4: CH3_rad_H
            L4: Cs/H2/OneDeN
        L3: OH_rad_H
        L3: Srad_H
        L3: N3s_rad_H
            L4: NH2_rad_H
            L4: N3s_rad_H_pri
                L5: N3s_rad_H/H/NonDeN
    L2: Xbirad_H
        L3: NH_triplet_H
        L3: NH_singlet_H
        L3: CH2_triplet_H
        L3: CH2_singlet_H
    L2: Xtrirad_H
        L3: C_quartet_H
        L3: C_doublet_H
L1: Y_rad_birad_trirad_quadrad
    L2: Y_1centerquadrad
        L3: C_quintet
        L3: C_triplet
        L3: C_singlet
    L2: Y_1centertrirad
        L3: N_atom_quartet
        L3: N_atom_doublet
        L3: CH_quartet
        L3: CH_doublet
    L2: Y_1centerbirad
        L3: O_atom_triplet
        L3: O_atom_singlet
        L3: NH_triplet
        L3: NH_singlet
        L3: CH2_triplet
        L3: CH2_singlet
    L2: Y_rad
        L3: H_rad
        L3: N3_rad
            L4: N3s_rad
                L5: NH2_rad
                L5: N3s_rad_pri
                L5: N3s_rad_sec
            L4: N3d_rad
                L5: N3d_rad/OneDe
                    L6: N3d_rad/OneDeC
                        L7: N3d_rad/OneDeCdd-O
        L3: N5_rad
            L4: N5d_rad
        L3: Y_2centeradjbirad
            L4: O2b
            L4: C2b
        L3: Ct_rad
            L4: Ct_rad/Ct
            L4: Ct_rad/N
        L3: O_rad
            L4: O_pri_rad
            L4: O_sec_rad
                L5: O_rad/NonDeC
                    L6: InChI=1/C4H9O/c1-4(2)3-5/h4H,3H2,1-2H3
                L5: O_rad/NonDeO
                    L6: OOCH3
                L5: O_rad/NonDeN
                L5: O_rad/OneDe
                    L6: O_rad/OneDeN
                    L6: InChI=1S/NO3/c2-1(3)4
                    L6: InChI=1/C4H7O/c1-2-3-4-5/h3-4H,2H2,1H3
                    L6: InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/o
        L3: S_rad
            L4: S_pri_rad
            L4: S_sec_rad
                L5: S_rad/NonDeC
                L5: S_rad/NonDeS
                L5: S_rad/OneDe
                    L6: S_rad/Cd
                        L7: S_rad/CS
                    L6: S_rad/Ct
                    L6: S_rad/Cb
                    L6: S_rad/CO
        L3: Cd_rad
            L4: Cd_pri_rad
                L5: InChI=1/C2H3/c1-2/h1H,2H2
                L5: InChI=1/C4H7/c1-3-4-2/h1,3H,4H2,2H3
            L4: Cd_sec_rad
                L5: Cd_rad/NonDeC
                    L6: InChI=1/C3H5/c1-3-2/h1H2,2H3
                    L6: InChI=1/C4H7/c1-3-4-2/h3H,1-2H3
                L5: Cd_rad/NonDeO
                L5: Cd_rad/NonDeS
                L5: Cd_rad/NonDeN
                L5: Cd_rad/OneDe
                    L6: Cd_rad/Cd
                        L7: Cd_rad/CS
                    L6: Cd_rad/Ct
                    L6: Cd_rad/Cb
                    L6: Cd_rad/CO
        L3: Cb_rad
        L3: CO_rad
            L4: CO_pri_rad
            L4: CO_sec_rad
                L5: CO_rad/NonDe
                L5: CO_rad/OneDe
        L3: CS_rad
            L4: CS_pri_rad
            L4: CS_sec_rad
                L5: CS_rad/NonDe
                    L6: CS_rad/Cs
                    L6: CS_rad/O
                    L6: CS_rad/S
                L5: CS_rad/OneDe
                    L6: CS_rad/Cd
                        L7: CS_rad/CS
                    L6: CS_rad/Ct
                    L6: CS_rad/Cb
                    L6: CS_rad/CO
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
                L5: C_rad/H2/S
                L5: C_rad/H2/N
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
                L5: C_rad/H/NonDeS
                    L6: C_rad/H/CsS
                    L6: C_rad/H/S2
                L5: C_rad/H/NonDeCN
                L5: C_rad/H/NonDeON
                L5: C_rad/H/NonDeNN
                L5: C_rad/H/OneDe
                    L6: C_rad/H/OneDeC
                        L7: C_rad/H/CdCs
                            L8: C_rad/H/CSCs
                        L7: C_rad/H/CtCs
                        L7: C_rad/H/CbCs
                        L7: C_rad/H/CO/Cs
                            L8: InChI=1/C3H5O/c1-2-3-4/h2-3H,1H3/c
                    L6: C_rad/H/OneDeO
                    L6: C_rad/H/OneDeS
                        L7: C_rad/H/CdS
                        L7: C_rad/H/CtS
                    L6: C_rad/H/OneDeN
                L5: C_rad/H/TwoDe
                    L6: C_rad/H/CdCd
                        L7: C_rad/H/CdCS
                        L7: C_rad/H/CSCS
                    L6: C_rad/H/CdCt
                        L7: C_rad/H/CtCS
                    L6: C_rad/H/CdCb
                        L7: C_rad/H/CbCS
                    L6: C_rad/H/CdCO
                        L7: C_rad/H/COCS
                    L6: C_rad/H/CtCt
                    L6: C_rad/H/CtCb
                    L6: C_rad/H/CtCO
                    L6: C_rad/H/CbCb
                    L6: C_rad/H/CbCO
                    L6: C_rad/H/COCO
            L4: C_ter_rad
                L5: C_rad/NonDe
                    L6: C_rad/Cs3
                        L7: InChI=1/C4H9O/c1-4(2)3-5/h5H,3H2,1-2H3
                    L6: C_rad/NDMustO
                        L7: C_rad/Cs2O
                            L8: C_rad/OOH/Cs/Cs
                            L8: InChI=1/C4H9O/c1-3-4(2)5/h5H,3H2,1-2H3
                        L7: C_rad/CsO2
                        L7: C_rad/O3
                    L6: C_rad/NDMustS
                        L7: C_rad/Cs2S
                        L7: C_rad/CsS2
                        L7: C_rad/S3
                L5: C_rad/OneDe
                    L6: C_rad/Cs2
                        L7: C_rad/CdCs2
                            L8: C_rad/CSCs2
                        L7: C_rad/CtCs2
                        L7: C_rad/CbCs2
                        L7: C_rad/COCs2
                    L6: C_rad/CsO
                    L6: C_rad/CsS
                        L7: C_rad/CdCsS
                        L7: C_rad/CtCsS
                    L6: C_rad/O2
                    L6: C_rad/OS
                    L6: C_rad/S2
                L5: C_rad/TwoDe
                    L6: C_rad/Cs
                        L7: C_rad/CdCdCs
                            L8: C_rad/CdCSCs
                            L8: C_rad/CSCSCs
                        L7: C_rad/CdCtCs
                            L8: C_rad/CtCSCs
                        L7: C_rad/CdCbCs
                            L8: C_rad/CbCSCs
                        L7: C_rad/CdCOCs
                            L8: C_rad/COCSCs
                        L7: C_rad/CtCtCs
                        L7: C_rad/CtCbCs
                        L7: C_rad/CtCOCs
                        L7: C_rad/CbCbCs
                        L7: C_rad/CbCOCs
                        L7: C_rad/COCOCs
                    L6: C_rad/TDMustO
                    L6: C_rad/TDMustS
                L5: C_rad/ThreeDe
"""
)

