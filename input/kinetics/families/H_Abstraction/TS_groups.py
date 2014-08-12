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
        distances = {'d12': 1.33174, 'd13': 2.65921, 'd23': 1.33213},
        uncertainties = {'d12': 0.079236, 'd13': 0.067233, 'd23': 0.078098},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1648 distances.
[<Entry index=47 label="CO/H/OneDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=61 label="C_methane">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=4 label="H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=203 label="OOC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=40 label="Cb_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=192 label="H_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=42 label="CO_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=4 label="H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=261 label="C_methyl">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=61 label="C_methane">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=13 label="ROOH_sec">, <Entry index=194 label="O2b">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=374 label="C_rad/CdCdCs">]
[<Entry index=4 label="H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=4 label="H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=16 label="Orad_O_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=40 label="Cb_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=203 label="OOC">]
[<Entry index=96 label="C/H2/O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=42 label="CO_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=232 label="Cd_Cd\H\Cs_rad/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=40 label="Cb_H">, <Entry index=192 label="H_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=4 label="H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=4 label="H2">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=261 label="C_methyl">]
[<Entry index=72 label="C/H3/O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=42 label="CO_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=192 label="H_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=192 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=61 label="C_methane">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=4 label="H2">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=192 label="H_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=443 label="OH_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=194 label="O2b">]
[<Entry index=77 label="C/H3/CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=7 label="O_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=7 label="O_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=198 label="O_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=198 label="O_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=261 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=194 label="O2b">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=16 label="Orad_O_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=4 label="H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=194 label="O2b">]
[<Entry index=42 label="CO_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/O">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=108 label="C/H2/OneDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=190 label="CH2_triplet">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=203 label="OOC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=261 label="C_methyl">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=67 label="C/H3/Cs\H2\Cs|O">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=7 label="O_pri">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=443 label="OH_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=192 label="H_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=42 label="CO_pri">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=241 label="Cb_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=42 label="CO_pri">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=61 label="C_methane">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=40 label="Cb_H">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=61 label="C_methane">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=198 label="O_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=198 label="O_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=72 label="C/H3/O">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=139 label="C/H/Cs2O">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=192 label="H_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H2/Cs\H2\Cs|Cs#O">]
[<Entry index=42 label="CO_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=178 label="C/H/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=306 label="C_rad/H/OneDeO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=61 label="C_methane">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=4 label="H2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=192 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=192 label="H_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=203 label="OOC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=241 label="Cb_rad">]
[<Entry index=4 label="H2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=443 label="OH_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=261 label="C_methyl">]
[<Entry index=40 label="Cb_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=241 label="Cb_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=198 label="O_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=72 label="C/H3/O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=203 label="OOC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=61 label="C_methane">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=61 label="C_methane">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=203 label="OOC">]
[<Entry index=72 label="C/H3/O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=61 label="C_methane">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=11 label="H2O2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=42 label="CO_pri">, <Entry index=190 label="CH2_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=335 label="C_rad/Cs2O">]
[<Entry index=7 label="O_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=203 label="OOC">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=4 label="H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=40 label="Cb_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=194 label="O2b">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=7 label="O_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=261 label="C_methyl">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=14 label="ROOH_ter">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=203 label="OOC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=203 label="OOC">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=241 label="Cb_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=40 label="Cb_H">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=198 label="O_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=16 label="Orad_O_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=194 label="O2b">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=61 label="C_methane">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=203 label="OOC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=72 label="C/H3/O">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=203 label="OOC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=192 label="H_rad">]
[<Entry index=61 label="C_methane">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=194 label="O2b">]
[<Entry index=443 label="OH_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=192 label="H_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="Cb_rad">]
[<Entry index=61 label="C_methane">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=454 label="O/H/OneDeC">, <Entry index=192 label="H_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=198 label="O_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=96 label="C/H2/O2">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=491 label="O_rad/OneDeC">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=203 label="OOC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=192 label="H_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=203 label="OOC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=203 label="OOC">]
[<Entry index=16 label="Orad_O_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/O">, <Entry index=194 label="O2b">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=7 label="O_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=40 label="Cb_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=40 label="Cb_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=61 label="C_methane">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
""",
)

entry(
    index = 2,
    label = "Y_rad_birad_trirad_quadrad",
    group = "OR{Y_2centeradjbirad, Y_1centerbirad, Y_rad, Y_1centertrirad, Y_1centerquadrad}",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "X_H",
    group = 
"""
1 *1 R u0 {2,S}
2 *2 H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.002603, 'd13': 0.000451, 'd23': 0.003144},
        uncertainties = {'d12': 0.078818, 'd13': 0.067047, 'd23': 0.078258},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1601 distances.
[<Entry index=47 label="CO/H/OneDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=61 label="C_methane">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=4 label="H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=203 label="OOC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=40 label="Cb_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=192 label="H_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=42 label="CO_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=4 label="H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=261 label="C_methyl">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=61 label="C_methane">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=13 label="ROOH_sec">, <Entry index=194 label="O2b">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=374 label="C_rad/CdCdCs">]
[<Entry index=4 label="H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=4 label="H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=16 label="Orad_O_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=40 label="Cb_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=203 label="OOC">]
[<Entry index=96 label="C/H2/O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=42 label="CO_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=232 label="Cd_Cd\H\Cs_rad/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=40 label="Cb_H">, <Entry index=192 label="H_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=4 label="H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=4 label="H2">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=261 label="C_methyl">]
[<Entry index=72 label="C/H3/O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=42 label="CO_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=192 label="H_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=192 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=61 label="C_methane">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=4 label="H2">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=192 label="H_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=11 label="H2O2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=194 label="O2b">]
[<Entry index=77 label="C/H3/CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=7 label="O_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=7 label="O_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=198 label="O_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=198 label="O_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=194 label="O2b">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=16 label="Orad_O_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=4 label="H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=194 label="O2b">]
[<Entry index=42 label="CO_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/O">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=108 label="C/H2/OneDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=190 label="CH2_triplet">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=203 label="OOC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=261 label="C_methyl">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=67 label="C/H3/Cs\H2\Cs|O">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=7 label="O_pri">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=192 label="H_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=42 label="CO_pri">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=241 label="Cb_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=42 label="CO_pri">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=61 label="C_methane">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=40 label="Cb_H">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=198 label="O_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=198 label="O_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=72 label="C/H3/O">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=139 label="C/H/Cs2O">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=192 label="H_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H2/Cs\H2\Cs|Cs#O">]
[<Entry index=42 label="CO_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=178 label="C/H/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=306 label="C_rad/H/OneDeO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=61 label="C_methane">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=4 label="H2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=192 label="H_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=203 label="OOC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=241 label="Cb_rad">]
[<Entry index=4 label="H2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=261 label="C_methyl">]
[<Entry index=40 label="Cb_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=241 label="Cb_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=198 label="O_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=72 label="C/H3/O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=203 label="OOC">]
[<Entry index=4 label="H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=4 label="H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=61 label="C_methane">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=61 label="C_methane">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=203 label="OOC">]
[<Entry index=61 label="C_methane">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=11 label="H2O2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=42 label="CO_pri">, <Entry index=190 label="CH2_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=335 label="C_rad/Cs2O">]
[<Entry index=7 label="O_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=203 label="OOC">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=4 label="H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=194 label="O2b">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=7 label="O_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=261 label="C_methyl">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=14 label="ROOH_ter">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=203 label="OOC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=203 label="OOC">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=241 label="Cb_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=72 label="C/H3/O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=40 label="Cb_H">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=198 label="O_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=16 label="Orad_O_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=194 label="O2b">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=61 label="C_methane">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=203 label="OOC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=72 label="C/H3/O">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=203 label="OOC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=192 label="H_rad">]
[<Entry index=61 label="C_methane">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=194 label="O2b">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=192 label="H_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="Cb_rad">]
[<Entry index=61 label="C_methane">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=454 label="O/H/OneDeC">, <Entry index=192 label="H_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=198 label="O_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=96 label="C/H2/O2">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=491 label="O_rad/OneDeC">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=203 label="OOC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=192 label="H_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=203 label="OOC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=203 label="OOC">]
[<Entry index=16 label="Orad_O_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/O">, <Entry index=194 label="O2b">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=7 label="O_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=40 label="Cb_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=40 label="Cb_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=61 label="C_methane">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
""",
)

entry(
    index = 4,
    label = "H2",
    group = 
"""
1 *1 H u0 {2,S}
2 *2 H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.330977, 'd13': -0.369666, 'd23': -0.04165},
        uncertainties = {'d12': 0.171848, 'd13': 0.14173, 'd23': 0.109413},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 64 distances.
[<Entry index=4 label="H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=4 label="H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=4 label="H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=4 label="H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H2/Cs\H2\Cs|Cs#O">]
[<Entry index=4 label="H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=4 label="H2">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=491 label="O_rad/OneDeC">]
[<Entry index=4 label="H2">, <Entry index=335 label="C_rad/Cs2O">]
[<Entry index=4 label="H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=4 label="H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=261 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=4 label="H2">, <Entry index=203 label="OOC">]
[<Entry index=4 label="H2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=241 label="Cb_rad">]
[<Entry index=4 label="H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=4 label="H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=4 label="H2">, <Entry index=232 label="Cd_Cd\H\Cs_rad/Cs">]
[<Entry index=4 label="H2">, <Entry index=190 label="CH2_triplet">]
""",
)

entry(
    index = 5,
    label = "Ct_H",
    group = 
"""
1 *1 Ct    u0 {2,S} {3,T}
2 *2 H     u0 {1,S}
3    [C,N] u0 {1,T}
""",
    distances = DistanceData(
        distances = {'d12': 0.411887, 'd13': 0.160102, 'd23': -0.1983},
        uncertainties = {'d12': 0.302233, 'd13': 0.297772, 'd23': 0.229993},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 6 distances.
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=241 label="Cb_rad">]
""",
)

entry(
    index = 457,
    label = "Ct/H/NonDeC",
    group = 
"""
1 *1 Ct u0 {2,S} {3,T}
2 *2 H  u0 {1,S}
3    Ct u0 {1,T}
""",
    distances = DistanceData(
        distances = {'d12': 0.411887, 'd13': 0.160102, 'd23': -0.1983},
        uncertainties = {'d12': 0.302233, 'd13': 0.297772, 'd23': 0.229993},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 6 distances.
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=241 label="Cb_rad">]
""",
)

entry(
    index = 458,
    label = "Ct/H/NonDeN",
    group = 
"""
1 *1 Ct  u0 {2,S} {3,T}
2 *2 H   u0 {1,S}
3    N3t u0 {1,T}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "O_H",
    group = 
"""
1 *1 O u0 {2,S} {3,S}
2 *2 H u0 {1,S}
3    R u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.094984, 'd13': -0.144158, 'd23': -0.044286},
        uncertainties = {'d12': 0.106482, 'd13': 0.082206, 'd23': 0.10198},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 171 distances.
[<Entry index=11 label="H2O2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=194 label="O2b">]
[<Entry index=11 label="H2O2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=192 label="H_rad">]
[<Entry index=7 label="O_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=11 label="H2O2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=7 label="O_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=194 label="O2b">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=192 label="H_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=203 label="OOC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="Cb_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=454 label="O/H/OneDeC">, <Entry index=192 label="H_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=203 label="OOC">]
[<Entry index=7 label="O_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=7 label="O_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=11 label="H2O2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=7 label="O_pri">, <Entry index=192 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=203 label="OOC">]
[<Entry index=7 label="O_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=261 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=14 label="ROOH_ter">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=11 label="H2O2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=13 label="ROOH_sec">, <Entry index=194 label="O2b">]
[<Entry index=11 label="H2O2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=7 label="O_pri">, <Entry index=261 label="C_methyl">]
""",
)

entry(
    index = 7,
    label = "O_pri",
    group = 
"""
1 *1 O u0 {2,S} {3,S}
2 *2 H u0 {1,S}
3    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.094464, 'd13': -0.134977, 'd23': -0.198842},
        uncertainties = {'d12': 0.175671, 'd13': 0.158411, 'd23': 0.064136},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 13 distances.
[<Entry index=7 label="O_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=7 label="O_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=7 label="O_pri">, <Entry index=192 label="H_rad">]
[<Entry index=7 label="O_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=7 label="O_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=7 label="O_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=7 label="O_pri">, <Entry index=261 label="C_methyl">]
""",
)

entry(
    index = 8,
    label = "O_sec",
    group = 
"""
1 *1 O   u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    R!H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.109539, 'd13': -0.144863, 'd23': -0.032412},
        uncertainties = {'d12': 0.101751, 'd13': 0.075827, 'd23': 0.104957},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 158 distances.
[<Entry index=11 label="H2O2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=194 label="O2b">]
[<Entry index=11 label="H2O2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=194 label="O2b">]
[<Entry index=11 label="H2O2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=192 label="H_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=11 label="H2O2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=192 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=203 label="OOC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="Cb_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=454 label="O/H/OneDeC">, <Entry index=192 label="H_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=203 label="OOC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=11 label="H2O2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=261 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=14 label="ROOH_ter">, <Entry index=261 label="C_methyl">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=11 label="H2O2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=11 label="H2O2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=13 label="ROOH_sec">, <Entry index=194 label="O2b">]
[<Entry index=11 label="H2O2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=243 label="CO_pri_rad">]
""",
)

entry(
    index = 9,
    label = "O/H/NonDeC",
    group = 
"""
1 *1 O  u0 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    Cs u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.052009, 'd13': -0.154128, 'd23': -0.097214},
        uncertainties = {'d12': 0.075539, 'd13': 0.071818, 'd23': 0.050142},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 44 distances.
[<Entry index=9 label="O/H/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
""",
)

entry(
    index = 10,
    label = "O/H/NonDeO",
    group = 
"""
1 *1 O u0 {2,S} {3,S}
2 *2 H u0 {1,S}
3    O u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.130355, 'd13': -0.140244, 'd23': -0.007724},
        uncertainties = {'d12': 0.111631, 'd13': 0.06362, 'd23': 0.113526},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 113 distances.
[<Entry index=10 label="O/H/NonDeO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=203 label="OOC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=261 label="C_methyl">]
[<Entry index=12 label="ROOH_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=192 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=194 label="O2b">]
[<Entry index=12 label="ROOH_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=14 label="ROOH_ter">, <Entry index=261 label="C_methyl">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="Cb_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=192 label="H_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=261 label="C_methyl">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=11 label="H2O2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=203 label="OOC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=11 label="H2O2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=194 label="O2b">]
[<Entry index=11 label="H2O2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=13 label="ROOH_sec">, <Entry index=194 label="O2b">]
[<Entry index=11 label="H2O2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=243 label="CO_pri_rad">]
""",
)

entry(
    index = 11,
    label = "H2O2",
    group = 
"""
1 *1 O u0 {2,S} {3,S}
2    O u0 {1,S} {4,S}
3 *2 H u0 {1,S}
4    H u0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.164676, 'd13': -0.140076, 'd23': 0.026736},
        uncertainties = {'d12': 0.075386, 'd13': 0.06591, 'd23': 0.118561},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 31 distances.
[<Entry index=11 label="H2O2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=11 label="H2O2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=261 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=11 label="H2O2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="Cb_rad">]
[<Entry index=11 label="H2O2">, <Entry index=192 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=11 label="H2O2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=243 label="CO_pri_rad">]
""",
)

entry(
    index = 12,
    label = "ROOH_pri",
    group = 
"""
1 *1 O  u0 {2,S} {7,S}
2    O  u0 {1,S} {3,S}
3    C  u0 {2,S} {4,S} {5,S} {6,S}
4    Cs u0 {3,S}
5    H  u0 {3,S}
6    H  u0 {3,S}
7 *2 H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.150698, 'd13': -0.133427, 'd23': 0.019412},
        uncertainties = {'d12': 0.046009, 'd13': 0.055076, 'd23': 0.079247},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 24 distances.
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=203 label="OOC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=194 label="O2b">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=275 label="C_rad/H2/Cd">]
""",
)

entry(
    index = 13,
    label = "ROOH_sec",
    group = 
"""
1 *1 O  u0 {2,S} {7,S}
2    O  u0 {1,S} {3,S}
3    C  u0 {2,S} {4,S} {5,S} {6,S}
4    Cs u0 {3,S}
5    Cs u0 {3,S}
6    H  u0 {3,S}
7 *2 H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.025951, 'd13': -0.172587, 'd23': -0.142422},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=13 label="ROOH_sec">, <Entry index=194 label="O2b">]
""",
)

entry(
    index = 14,
    label = "ROOH_ter",
    group = 
"""
1 *1 O  u0 {2,S} {7,S}
2    O  u0 {1,S} {3,S}
3    C  u0 {2,S} {4,S} {5,S} {6,S}
4    Cs u0 {3,S}
5    Cs u0 {3,S}
6    Cs u0 {3,S}
7 *2 H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.209906, 'd13': -0.111168, 'd23': 0.096008},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=14 label="ROOH_ter">, <Entry index=261 label="C_methyl">]
""",
)

entry(
    index = 471,
    label = "O/H/NonDeN",
    group = 
"""
1 *1 O   u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    N3s u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "O/H/OneDe",
    group = 
"""
1 *1 O                        u0 {2,S} {3,S}
2 *2 H                        u0 {1,S}
3    [Cd,Ct,Cb,CO,CS,N3d,N5d] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.238138, 'd13': -0.375325, 'd23': -0.133518},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=454 label="O/H/OneDeC">, <Entry index=192 label="H_rad">]
""",
)

entry(
    index = 454,
    label = "O/H/OneDeC",
    group = 
"""
1 *1 O                u0 {2,S} {3,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.238138, 'd13': -0.375325, 'd23': -0.133518},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=454 label="O/H/OneDeC">, <Entry index=192 label="H_rad">]
""",
)

entry(
    index = 455,
    label = "O/H/OneDeN",
    group = 
"""
1 *1 O         u0 {2,S} {3,S}
2 *2 H         u0 {1,S}
3    [N3d,N5d] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "Orad_O_H",
    group = 
"""
1 *1 O u0 {2,S} {3,S}
2 *2 H u0 {1,S}
3    O u1 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.246399, 'd13': -0.050484, 'd23': 0.198886},
        uncertainties = {'d12': 0.06584, 'd13': 0.127855, 'd23': 0.174379},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 18 distances.
[<Entry index=16 label="Orad_O_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=16 label="Orad_O_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=203 label="OOC">]
[<Entry index=16 label="Orad_O_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
""",
)

entry(
    index = 17,
    label = "S_H",
    group = 
"""
1 *1 S u0 {2,S} {3,S}
2 *2 H u0 {1,S}
3    R u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "S_pri",
    group = 
"""
1 *1 S u0 {2,S} {3,S}
2 *2 H u0 {1,S}
3    H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "S_sec",
    group = 
"""
1 *1 S   u0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    R!H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "S/H/NonDeC",
    group = 
"""
1 *1 S  u0 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "S/H/NonDeS",
    group = 
"""
1 *1 S u0 {2,S} {3,S}
2 *2 H u0 {1,S}
3    S u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "S/H/OneDe",
    group = 
"""
1 *1 S                u0 {2,S} {3,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "S/H/Ct",
    group = 
"""
1 *1 S  u0 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "S/H/Cb",
    group = 
"""
1 *1 S  u0 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "S/H/CO",
    group = 
"""
1 *1 S  u0 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    CO u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "S/H/Cd",
    group = 
"""
1 *1 S  u0 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    Cd u0 {1,S} {4,D}
4    C  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "S/H/CS",
    group = 
"""
1 *1 S  u0 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    CS u0 {1,S} {4,D}
4    S  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "Cd_H",
    group = 
"""
1 *1 C     u0 {2,D} {3,S} {4,S}
2    [C,N] u0 {1,D}
3 *2 H     u0 {1,S}
4    R     u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.085759, 'd13': 0.012835, 'd23': -0.073553},
        uncertainties = {'d12': 0.131005, 'd13': 0.086739, 'd23': 0.107921},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 148 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=198 label="O_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
""",
)

entry(
    index = 29,
    label = "Cd_pri",
    group = 
"""
1 *1 C     u0 {2,D} {3,S} {4,S}
2    [C,N] u0 {1,D}
3 *2 H     u0 {1,S}
4    H     u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.08298, 'd13': 0.014923, 'd23': -0.068322},
        uncertainties = {'d12': 0.130875, 'd13': 0.078277, 'd23': 0.10775},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 125 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=189 label="O_atom_triplet">]
""",
)

entry(
    index = 459,
    label = "Cd/H2/NonDeC",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    C u0 {1,D}
3 *2 H u0 {1,S}
4    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.08298, 'd13': 0.014923, 'd23': -0.068322},
        uncertainties = {'d12': 0.130875, 'd13': 0.078277, 'd23': 0.10775},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 125 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=189 label="O_atom_triplet">]
""",
)

entry(
    index = 460,
    label = "Cd/H2/NonDeN",
    group = 
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    N3d u0 {1,D}
3 *2 H   u0 {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "Cd_sec",
    group = 
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    C   u0 {1,D}
3 *2 H   u0 {1,S}
4    R!H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.102936, 'd13': -7e-05, 'd23': -0.105888},
        uncertainties = {'d12': 0.142471, 'd13': 0.132084, 'd23': 0.117723},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 23 distances.
[<Entry index=35 label="Cd/H/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=198 label="O_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=192 label="H_rad">]
""",
)

entry(
    index = 31,
    label = "Cd/H/NonDeC",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    C  u0 {1,D}
3 *2 H  u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.129757, 'd13': -0.052539, 'd23': -0.185595},
        uncertainties = {'d12': 0.050505, 'd13': 0.297565, 'd23': 0.287462},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 4 distances.
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=192 label="H_rad">]
""",
)

entry(
    index = 32,
    label = "Cd/H/NonDeO",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    C u0 {1,D}
3 *2 H u0 {1,S}
4    O u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "Cd/H/NonDeS",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    C u0 {1,D}
3 *2 H u0 {1,S}
4    S u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 404,
    label = "Cd/H/NonDeN",
    group = 
"""
1 *1 C         u0 {2,D} {3,S} {4,S}
2    C         u0 {1,D}
3 *2 H         u0 {1,S}
4    [N3s,N5s] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "Cd/H/OneDe",
    group = 
"""
1 *1 C                  u0 {2,D} {3,S} {4,S}
2    C                  u0 {1,D}
3 *2 H                  u0 {1,S}
4    [Cd,Ct,Cb,CO,CS,N] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.097766, 'd13': 0.010044, 'd23': -0.090523},
        uncertainties = {'d12': 0.15898, 'd13': 0.124303, 'd23': 0.106681},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 19 distances.
[<Entry index=35 label="Cd/H/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=198 label="O_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=200 label="O_rad/NonDeC">]
""",
)

entry(
    index = 35,
    label = "Cd/H/Ct",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    C  u0 {1,D}
3 *2 H  u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.025331, 'd13': -0.071388, 'd23': -0.047885},
        uncertainties = {'d12': 0.177084, 'd13': 0.333532, 'd23': 0.198348},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=35 label="Cd/H/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=224 label="Cd_pri_rad">]
""",
)

entry(
    index = 36,
    label = "Cd/H/Cb",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    C  u0 {1,D}
3 *2 H  u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "Cd/H/CO",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    C  u0 {1,D}
3 *2 H  u0 {1,S}
4    CO u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "Cd/H/Cd",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    C  u0 {1,D}
3 *2 H  u0 {1,S}
4    Cd u0 {1,S} {5,D}
5    C  u0 {4,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.116572, 'd13': 0.022485, 'd23': -0.097038},
        uncertainties = {'d12': 0.173757, 'd13': 0.124276, 'd23': 0.113003},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 16 distances.
[<Entry index=38 label="Cd/H/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=198 label="O_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=200 label="O_rad/NonDeC">]
""",
)

entry(
    index = 39,
    label = "Cd/H/CS",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    C  u0 {1,D}
3 *2 H  u0 {1,S}
4    Cd u0 {1,S} {5,D}
5    S  u0 {4,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 405,
    label = "Cd/H/DeN",
    group = 
"""
1 *1 C                              u0 {2,D} {3,S} {4,S}
2    C                              u0 {1,D}
3 *2 H                              u0 {1,S}
4    [N3d,N3t,N3b,N5d,N5dd,N5t,N5b] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "Cb_H",
    group = 
"""
1 *1 Cb       u0 {2,B} {3,B} {4,S}
2    [Cb,Cbf] u0 {1,B}
3    [Cb,Cbf] u0 {1,B}
4 *2 H        u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.121038, 'd13': 0.031404, 'd23': -0.088806},
        uncertainties = {'d12': 0.11145, 'd13': 0.095845, 'd23': 0.091871},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 29 distances.
[<Entry index=40 label="Cb_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=192 label="H_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=40 label="Cb_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=40 label="Cb_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=40 label="Cb_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=40 label="Cb_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=261 label="C_methyl">]
[<Entry index=40 label="Cb_H">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=40 label="Cb_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=40 label="Cb_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=198 label="O_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=203 label="OOC">]
[<Entry index=40 label="Cb_H">, <Entry index=280 label="C_rad/H/NonDeC">]
""",
)

entry(
    index = 41,
    label = "CO_H",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    O u0 {1,D}
3 *2 H u0 {1,S}
4    R u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.012139, 'd13': 0.058536, 'd23': 0.047424},
        uncertainties = {'d12': 0.054157, 'd13': 0.047369, 'd23': 0.081673},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 129 distances.
[<Entry index=47 label="CO/H/OneDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=203 label="OOC">]
[<Entry index=42 label="CO_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=194 label="O2b">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=42 label="CO_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=42 label="CO_pri">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=203 label="OOC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=192 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=42 label="CO_pri">, <Entry index=261 label="C_methyl">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=42 label="CO_pri">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=42 label="CO_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=42 label="CO_pri">, <Entry index=192 label="H_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=203 label="OOC">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=42 label="CO_pri">, <Entry index=190 label="CH2_triplet">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=261 label="C_methyl">]
""",
)

entry(
    index = 42,
    label = "CO_pri",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    O u0 {1,D}
3 *2 H u0 {1,S}
4    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.014276, 'd13': 0.050741, 'd23': 0.036093},
        uncertainties = {'d12': 0.054471, 'd13': 0.042365, 'd23': 0.074013},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 41 distances.
[<Entry index=42 label="CO_pri">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=42 label="CO_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=42 label="CO_pri">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=42 label="CO_pri">, <Entry index=194 label="O2b">]
[<Entry index=42 label="CO_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=42 label="CO_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=42 label="CO_pri">, <Entry index=261 label="C_methyl">]
[<Entry index=42 label="CO_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=42 label="CO_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=42 label="CO_pri">, <Entry index=192 label="H_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=42 label="CO_pri">, <Entry index=203 label="OOC">]
[<Entry index=42 label="CO_pri">, <Entry index=190 label="CH2_triplet">]
""",
)

entry(
    index = 43,
    label = "CO_sec",
    group = 
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    O   u0 {1,D}
3 *2 H   u0 {1,S}
4    R!H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.011113, 'd13': 0.062278, 'd23': 0.052863},
        uncertainties = {'d12': 0.05509, 'd13': 0.050329, 'd23': 0.086411},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 88 distances.
[<Entry index=47 label="CO/H/OneDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=203 label="OOC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=203 label="OOC">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=192 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=261 label="C_methyl">]
""",
)

entry(
    index = 44,
    label = "CO/H/NonDe",
    group = 
"""
1 *1 C        u0 {2,D} {3,S} {4,S}
2    O        u0 {1,D}
3 *2 H        u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.003408, 'd13': 0.065949, 'd23': 0.062876},
        uncertainties = {'d12': 0.057883, 'd13': 0.055718, 'd23': 0.101708},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 54 distances.
[<Entry index=45 label="CO/H/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=203 label="OOC">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=192 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=261 label="C_methyl">]
""",
)

entry(
    index = 45,
    label = "CO/H/Cs",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    O  u0 {1,D}
3 *2 H  u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.003409, 'd13': 0.071115, 'd23': 0.068336},
        uncertainties = {'d12': 0.056403, 'd13': 0.051753, 'd23': 0.094179},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 49 distances.
[<Entry index=45 label="CO/H/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=203 label="OOC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=261 label="C_methyl">]
""",
)

entry(
    index = 46,
    label = "CO/H/Cs\Cs|Cs",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    O  u0 {1,D}
3 *2 H  u0 {1,S}
4    Cs u0 {1,S} {5,S}
5    Cs u0 {4,S} {6,S}
6    Cs u0 {5,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.032858, 'd13': 0.094783, 'd23': 0.125737},
        uncertainties = {'d12': 0.110262, 'd13': 0.031779, 'd23': 0.13513},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 6 distances.
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=261 label="C_methyl">]
""",
)

entry(
    index = 47,
    label = "CO/H/OneDe",
    group = 
"""
1 *1 C             u0 {2,D} {3,S} {4,S}
2    O             u0 {1,D}
3 *2 H             u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.022371, 'd13': 0.056915, 'd23': 0.038232},
        uncertainties = {'d12': 0.053353, 'd13': 0.043207, 'd23': 0.059429},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 34 distances.
[<Entry index=47 label="CO/H/OneDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=203 label="OOC">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=261 label="C_methyl">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
""",
)

entry(
    index = 48,
    label = "CS_H",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    S u0 {1,D}
3 *2 H u0 {1,S}
4    R u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "CS_pri",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    S u0 {1,D}
3 *2 H u0 {1,S}
4    H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "CS_sec",
    group = 
"""
1 *1 C   u0 {2,D} {3,S} {4,S}
2    S   u0 {1,D}
3 *2 H   u0 {1,S}
4    R!H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "CS/H/NonDeC",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    S  u0 {1,D}
3 *2 H  u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "CS/H/NonDeO",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    S u0 {1,D}
3 *2 H u0 {1,S}
4    O u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "CS/H/NonDeS",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2    S u0 {1,D}
3 *2 H u0 {1,S}
4    S u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "CS/H/OneDe",
    group = 
"""
1 *1 C                u0 {2,D} {3,S} {4,S}
2    S                u0 {1,D}
3 *2 H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "CS/H/Ct",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    S  u0 {1,D}
3 *2 H  u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "CS/H/Cb",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    S  u0 {1,D}
3 *2 H  u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "CS/H/CO",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    S  u0 {1,D}
3 *2 H  u0 {1,S}
4    CO u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "CS/H/Cd",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    S  u0 {1,D}
3 *2 H  u0 {1,S}
4    Cd u0 {1,S} {5,D}
5    C  u0 {4,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "CS/H/CS",
    group = 
"""
1 *1 C  u0 {2,D} {3,S} {4,S}
2    S  u0 {1,D}
3 *2 H  u0 {1,S}
4    CS u0 {1,S} {5,D}
5    S  u0 {4,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "Cs_H",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 {1,S}
3    R u0 {1,S}
4    R u0 {1,S}
5    R u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.018064, 'd13': 0.036652, 'd23': 0.017674},
        uncertainties = {'d12': 0.051487, 'd13': 0.051409, 'd23': 0.062066},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1036 distances.
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=61 label="C_methane">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=203 label="OOC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=72 label="C/H3/O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=61 label="C_methane">, <Entry index=374 label="C_rad/CdCdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=61 label="C_methane">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=96 label="C/H2/O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=61 label="C_methane">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=72 label="C/H3/O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=192 label="H_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=61 label="C_methane">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=241 label="Cb_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=192 label="H_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=194 label="O2b">]
[<Entry index=77 label="C/H3/CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=198 label="O_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=198 label="O_pri_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=72 label="C/H3/O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=72 label="C/H3/O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=194 label="O2b">]
[<Entry index=72 label="C/H3/O">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=203 label="OOC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=190 label="CH2_triplet">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=203 label="OOC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=261 label="C_methyl">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=67 label="C/H3/Cs\H2\Cs|O">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=192 label="H_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=241 label="Cb_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=61 label="C_methane">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=61 label="C_methane">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=198 label="O_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=203 label="OOC">]
[<Entry index=139 label="C/H/Cs2O">, <Entry index=192 label="H_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=194 label="O2b">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=192 label="H_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=178 label="C/H/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=203 label="OOC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=306 label="C_rad/H/OneDeO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=61 label="C_methane">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=192 label="H_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=241 label="Cb_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=61 label="C_methane">, <Entry index=241 label="Cb_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=72 label="C/H3/O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=61 label="C_methane">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=190 label="CH2_triplet">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=203 label="OOC">]
[<Entry index=61 label="C_methane">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=61 label="C_methane">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=61 label="C_methane">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=61 label="C_methane">, <Entry index=203 label="OOC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=203 label="OOC">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=241 label="Cb_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=72 label="C/H3/O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=194 label="O2b">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=61 label="C_methane">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=198 label="O_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=203 label="OOC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=194 label="O2b">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=192 label="H_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=261 label="C_methyl">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=192 label="H_rad">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=198 label="O_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=96 label="C/H2/O2">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=108 label="C/H2/OneDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=203 label="OOC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=192 label="H_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/O">, <Entry index=261 label="C_methyl">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=261 label="C_methyl">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=61 label="C_methane">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
""",
)

entry(
    index = 61,
    label = "C_methane",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
5    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.08473, 'd13': 0.033098, 'd23': -0.055468},
        uncertainties = {'d12': 0.061896, 'd13': 0.044296, 'd23': 0.042835},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 69 distances.
[<Entry index=61 label="C_methane">, <Entry index=241 label="Cb_rad">]
[<Entry index=61 label="C_methane">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=61 label="C_methane">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=374 label="C_rad/CdCdCs">]
[<Entry index=61 label="C_methane">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=61 label="C_methane">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=61 label="C_methane">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=61 label="C_methane">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=61 label="C_methane">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=61 label="C_methane">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=61 label="C_methane">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=61 label="C_methane">, <Entry index=203 label="OOC">]
[<Entry index=61 label="C_methane">, <Entry index=198 label="O_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=61 label="C_methane">, <Entry index=192 label="H_rad">]
[<Entry index=61 label="C_methane">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=61 label="C_methane">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=61 label="C_methane">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=61 label="C_methane">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=61 label="C_methane">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=61 label="C_methane">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=61 label="C_methane">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=224 label="Cd_pri_rad">]
""",
)

entry(
    index = 62,
    label = "C_pri",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    R!H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.035204, 'd13': 0.029334, 'd23': -0.007234},
        uncertainties = {'d12': 0.04953, 'd13': 0.043267, 'd23': 0.054362},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 543 distances.
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=203 label="OOC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=194 label="O2b">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=198 label="O_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=203 label="OOC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=306 label="C_rad/H/OneDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=77 label="C/H3/CO">, <Entry index=194 label="O2b">]
[<Entry index=72 label="C/H3/O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=77 label="C/H3/CO">, <Entry index=192 label="H_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=72 label="C/H3/O">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=72 label="C/H3/O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=192 label="H_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=198 label="O_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=72 label="C/H3/O">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=190 label="CH2_triplet">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=67 label="C/H3/Cs\H2\Cs|O">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=203 label="OOC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=241 label="Cb_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=198 label="O_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/O">, <Entry index=261 label="C_methyl">]
[<Entry index=72 label="C/H3/O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=203 label="OOC">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=72 label="C/H3/O">, <Entry index=194 label="O2b">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=77 label="C/H3/CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
""",
)

entry(
    index = 63,
    label = "C/H3/Cs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.061457, 'd13': 0.026045, 'd23': -0.038279},
        uncertainties = {'d12': 0.044984, 'd13': 0.048025, 'd23': 0.052957},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 277 distances.
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=203 label="OOC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=306 label="C_rad/H/OneDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=198 label="O_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=203 label="OOC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=198 label="O_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=190 label="CH2_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=67 label="C/H3/Cs\H2\Cs|O">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=203 label="OOC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=198 label="O_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
""",
)

entry(
    index = 64,
    label = "C/H3/Cs\H3",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    H  u0 {2,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.057492, 'd13': 0.031751, 'd23': -0.029212},
        uncertainties = {'d12': 0.056276, 'd13': 0.036178, 'd23': 0.05158},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 57 distances.
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=198 label="O_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=306 label="C_rad/H/OneDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
""",
)

entry(
    index = 65,
    label = "C/H3/Cs\OneNonDe",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H        u0 {1,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    H        u0 {2,S}
8    H        u0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.065557, 'd13': 0.020233, 'd23': -0.048054},
        uncertainties = {'d12': 0.042201, 'd13': 0.066023, 'd23': 0.064143},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 87 distances.
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=198 label="O_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=203 label="OOC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=67 label="C/H3/Cs\H2\Cs|O">, <Entry index=192 label="H_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=192 label="H_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=192 label="H_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=243 label="CO_pri_rad">]
""",
)

entry(
    index = 66,
    label = "C/H3/Cs\H2\Cs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cs u0 {2,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.061093, 'd13': 0.013862, 'd23': -0.050484},
        uncertainties = {'d12': 0.041114, 'd13': 0.081951, 'd23': 0.075588},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 51 distances.
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=67 label="C/H3/Cs\H2\Cs|O">, <Entry index=192 label="H_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=192 label="H_rad">]
""",
)

entry(
    index = 67,
    label = "C/H3/Cs\H2\Cs|O",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cs u0 {2,S} {9,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
9    O  u0 {6,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.048523, 'd13': -0.238721, 'd23': -0.290862},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=67 label="C/H3/Cs\H2\Cs|O">, <Entry index=192 label="H_rad">]
""",
)

entry(
    index = 68,
    label = "C/H3/Cs\H2\O",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    O  u0 {2,S}
7    H  u0 {2,S}
8    H  u0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.071652, 'd13': 0.028928, 'd23': -0.044737},
        uncertainties = {'d12': 0.045791, 'd13': 0.036996, 'd23': 0.046954},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 36 distances.
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=198 label="O_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=203 label="OOC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=192 label="H_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
""",
)

entry(
    index = 69,
    label = "C/H3/Cs\TwoNonDe",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2    Cs       u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H        u0 {1,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6    [Cs,O,S] u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    H        u0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.06024, 'd13': 0.026008, 'd23': -0.037527},
        uncertainties = {'d12': 0.049623, 'd13': 0.043276, 'd23': 0.051767},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 37 distances.
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=190 label="CH2_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=198 label="O_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=203 label="OOC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=304 label="C_rad/H/CdCs">]
""",
)

entry(
    index = 70,
    label = "C/H3/Cs\H\Cs\O",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cs u0 {2,S}
7    O  u0 {2,S}
8    H  u0 {2,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "C/H3/Cs\H\Cs\Cs|O",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {6,S} {7,S} {8,S}
3 *2 H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
6    Cs u0 {2,S} {9,S}
7    Cs u0 {2,S}
8    H  u0 {2,S}
9    O  u0 {6,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "C/H3/O",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
5    O u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.031353, 'd13': 0.025802, 'd23': 0.00099},
        uncertainties = {'d12': 0.045476, 'd13': 0.033225, 'd23': 0.049886},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 48 distances.
[<Entry index=72 label="C/H3/O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=72 label="C/H3/O">, <Entry index=192 label="H_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=72 label="C/H3/O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=72 label="C/H3/O">, <Entry index=261 label="C_methyl">]
[<Entry index=72 label="C/H3/O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=72 label="C/H3/O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=72 label="C/H3/O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=72 label="C/H3/O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=72 label="C/H3/O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=203 label="OOC">]
[<Entry index=72 label="C/H3/O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=72 label="C/H3/O">, <Entry index=194 label="O2b">]
[<Entry index=72 label="C/H3/O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/O">, <Entry index=241 label="Cb_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=275 label="C_rad/H2/Cd">]
""",
)

entry(
    index = 73,
    label = "C/H3/S",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
5    S u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "C/H3/OneDe",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    H                u0 {1,S}
4    H                u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.004483, 'd13': 0.034003, 'd23': 0.028343},
        uncertainties = {'d12': 0.056203, 'd13': 0.039209, 'd23': 0.057777},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 218 distances.
[<Entry index=77 label="C/H3/CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=194 label="O2b">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=194 label="O2b">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=77 label="C/H3/CO">, <Entry index=192 label="H_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=261 label="C_methyl">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=190 label="CH2_triplet">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=77 label="C/H3/CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=203 label="OOC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=192 label="H_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=243 label="CO_pri_rad">]
""",
)

entry(
    index = 75,
    label = "C/H3/Ct",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.010667, 'd13': 0.026906, 'd23': 0.013106},
        uncertainties = {'d12': 0.048605, 'd13': 0.025208, 'd23': 0.045868},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 27 distances.
[<Entry index=75 label="C/H3/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=203 label="OOC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=190 label="CH2_triplet">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
""",
)

entry(
    index = 76,
    label = "C/H3/Cb",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "C/H3/CO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    CO u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.031307, 'd13': 0.020037, 'd23': -0.009158},
        uncertainties = {'d12': 0.062315, 'd13': 0.03694, 'd23': 0.046487},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 63 distances.
[<Entry index=77 label="C/H3/CO">, <Entry index=194 label="O2b">]
[<Entry index=77 label="C/H3/CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=192 label="H_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=203 label="OOC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=261 label="C_methyl">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
""",
)

entry(
    index = 78,
    label = "C/H3/Cd",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cd u0 {1,S} {6,D}
6    C  u0 {5,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.009496, 'd13': 0.04208, 'd23': 0.049244},
        uncertainties = {'d12': 0.055987, 'd13': 0.043295, 'd23': 0.0657},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 128 distances.
[<Entry index=78 label="C/H3/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=194 label="O2b">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=192 label="H_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=246 label="CO_rad/OneDe">]
""",
)

entry(
    index = 79,
    label = "C/H3/Cd\H_Cd\H2",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cd u0 {1,S} {6,D} {7,S}
6    Cd u0 {5,D} {8,S} {9,S}
7    H  u0 {5,S}
8    H  u0 {6,S}
9    H  u0 {6,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.012445, 'd13': 0.032692, 'd23': 0.042971},
        uncertainties = {'d12': 0.041214, 'd13': 0.03407, 'd23': 0.036053},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 39 distances.
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=194 label="O2b">]
""",
)

entry(
    index = 80,
    label = "C/H3/Cd\H_Cd\H\Cs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cd u0 {1,S} {6,D} {7,S}
6    Cd u0 {5,D} {8,S} {9,S}
7    H  u0 {5,S}
8    Cs u0 {6,S}
9    H  u0 {6,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.038358, 'd13': 0.037821, 'd23': 0.072682},
        uncertainties = {'d12': 0.116256, 'd13': 0.154305, 'd23': 0.072722},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=261 label="C_methyl">]
""",
)

entry(
    index = 81,
    label = "C/H3/Cd\Cs_Cd\H2",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    Cd u0 {1,S} {6,D} {7,S}
6    Cd u0 {5,D} {8,S} {9,S}
7    Cs u0 {5,S}
8    H  u0 {6,S}
9    H  u0 {6,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.019358, 'd13': 0.014981, 'd23': 0.029762},
        uncertainties = {'d12': 0.092119, 'd13': 0.185315, 'd23': 0.104352},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=194 label="O2b">]
""",
)

entry(
    index = 82,
    label = "C/H3/CS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    CS u0 {1,S} {6,D}
6    S  u0 {5,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 461,
    label = "Cs/H3/NonDeN",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2    N3s u0 {1,S}
3 *2 H   u0 {1,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 471,
    label = "Cs/H3/OneDeN",
    group = 
"""
1 *1 C         u0 {2,S} {3,S} {4,S} {5,S}
2    [N3d,N5d] u0 {1,S}
3 *2 H         u0 {1,S}
4    H         u0 {1,S}
5    H         u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "C_sec",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.014242, 'd13': 0.046384, 'd23': 0.060465},
        uncertainties = {'d12': 0.054556, 'd13': 0.058228, 'd23': 0.073741},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 333 distances.
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=261 label="C_methyl">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=194 label="O2b">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=203 label="OOC">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=261 label="C_methyl">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=192 label="H_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=96 label="C/H2/O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=261 label="C_methyl">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=192 label="H_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=96 label="C/H2/O2">, <Entry index=261 label="C_methyl">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=108 label="C/H2/OneDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=203 label="OOC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=192 label="H_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=192 label="H_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=261 label="C_methyl">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=241 label="Cb_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=241 label="Cb_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
""",
)

entry(
    index = 84,
    label = "C/H2/NonDeC",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.037911, 'd13': 0.013557, 'd23': -0.027585},
        uncertainties = {'d12': 0.054823, 'd13': 0.039054, 'd23': 0.048763},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 62 distances.
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=241 label="Cb_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=192 label="H_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=261 label="C_methyl">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
""",
)

entry(
    index = 85,
    label = "C/H2/Cs/Cs\O",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S} {6,S}
6    O  u0 {5,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "C/H2/Cs/Cs\Cs|O",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S} {6,S}
6    Cs u0 {5,S} {7,S}
7    O  u0 {6,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "C/H2/NonDeC_5ring",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cs u0 {1,S} {6,S}
5    Cs u0 {1,S} {7,S}
6    Cs u0 {4,S} {7,S}
7    Cs u0 {5,S} {6,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.011911, 'd13': -0.021447, 'd23': -0.013819},
        uncertainties = {'d12': 0.077907, 'd13': 0.125657, 'd23': 0.060341},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 5 distances.
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=261 label="C_methyl">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=192 label="H_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=241 label="Cb_rad">]
""",
)

entry(
    index = 88,
    label = "C/H2/NonDeC_5ring_fused6_1",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cs u0 {1,S} {6,S} {8,S}
5    Cs u0 {1,S} {7,S}
6    Cs u0 {4,S} {7,S}
7    Cs u0 {5,S} {6,S} {9,S}
8    Cs u0 {4,S} {9,S}
9    Cs u0 {7,S} {8,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "C/H2/NonDeC_5ring_fused6_2",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cs u0 {1,S} {6,S} {8,S}
5    Cs u0 {1,S} {7,S} {9,S}
6    Cs u0 {4,S} {7,S}
7    Cs u0 {5,S} {6,S}
8    Cs u0 {4,S} {9,S}
9    Cs u0 {5,S} {8,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "C/H2/NonDeC_5ring_alpha6ring",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2  *2 H  u0 {1,S}
3     H  u0 {1,S}
4     Cs u0 {1,S} {6,S} {8,S}
5     Cs u0 {1,S} {7,S}
6     Cs u0 {4,S} {7,S} {11,S}
7     Cs u0 {5,S} {6,S}
8     C  u0 {4,S} {9,S}
9     C  u0 {8,S} {10,S}
10    C  u0 {9,S} {11,S}
11    C  u0 {6,S} {10,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "C/H2/NonDeC_5ring_beta6ring",
    group = 
"""
1  *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2  *2 H  u0 {1,S}
3     H  u0 {1,S}
4     Cs u0 {1,S} {6,S}
5     Cs u0 {1,S} {7,S}
6     Cs u0 {4,S} {7,S} {8,S}
7     Cs u0 {5,S} {6,S} {11,S}
8     C  u0 {6,S} {9,S}
9     C  u0 {8,S} {10,S}
10    C  u0 {9,S} {11,S}
11    C  u0 {7,S} {10,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "C/H2/Cs\H3/Cs\H3",
    group = 
"""
1     Cs u0 {2,S} {4,S} {5,S} {6,S}
2  *1 C  u0 {1,S} {3,S} {7,S} {8,S}
3     Cs u0 {2,S} {9,S} {10,S} {11,S}
4     H  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7  *2 H  u0 {2,S}
8     H  u0 {2,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.051732, 'd13': 0.035243, 'd23': -0.019498},
        uncertainties = {'d12': 0.052271, 'd13': 0.032578, 'd23': 0.038075},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 42 distances.
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
""",
)

entry(
    index = 93,
    label = "C/H2/NonDeO",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        u0 {1,S}
3    H        u0 {1,S}
4    O        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.024133, 'd13': 0.029195, 'd23': 0.012452},
        uncertainties = {'d12': 0.056404, 'd13': 0.044259, 'd23': 0.075469},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 43 distances.
[<Entry index=94 label="C/H2/CsO">, <Entry index=261 label="C_methyl">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=96 label="C/H2/O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=192 label="H_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=96 label="C/H2/O2">, <Entry index=261 label="C_methyl">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
""",
)

entry(
    index = 94,
    label = "C/H2/CsO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    O  u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.023452, 'd13': 0.029559, 'd23': 0.013849},
        uncertainties = {'d12': 0.056238, 'd13': 0.044915, 'd23': 0.075136},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 41 distances.
[<Entry index=94 label="C/H2/CsO">, <Entry index=261 label="C_methyl">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=192 label="H_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=200 label="O_rad/NonDeC">]
""",
)

entry(
    index = 95,
    label = "C/H2/Cs\Cs2/O",
    group = 
"""
1     C  u0 {2,S} {6,S} {7,S} {8,S}
2     Cs u0 {1,S} {3,S} {5,S} {9,S}
3  *1 C  u0 {2,S} {4,S} {10,S} {11,S}
4     O  u0 {3,S} {12,S}
5     C  u0 {2,S} {13,S} {14,S} {15,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {1,S}
9     H  u0 {2,S}
10 *2 H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    H  u0 {5,S}
14    H  u0 {5,S}
15    H  u0 {5,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "C/H2/O2",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 {1,S}
3    H u0 {1,S}
4    O u0 {1,S}
5    O u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.039113, 'd13': 0.021172, 'd23': -0.018286},
        uncertainties = {'d12': 0.544645, 'd13': 0.268233, 'd23': 0.746833},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=96 label="C/H2/O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=96 label="C/H2/O2">, <Entry index=261 label="C_methyl">]
""",
)

entry(
    index = 97,
    label = "C/H2/NonDeS",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        u0 {1,S}
3    H        u0 {1,S}
4    S        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "C/H2/CsS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 407,
    label = "C/H2/NonDeN",
    group = 
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H          u0 {1,S}
3    H          u0 {1,S}
4    N          u0 {1,S}
5    [Cs,O,S,N] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "C/H2/OneDe",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,Cb,CS] u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.024373, 'd13': 0.049717, 'd23': 0.073316},
        uncertainties = {'d12': 0.057174, 'd13': 0.054298, 'd23': 0.073968},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 143 distances.
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=261 label="C_methyl">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=108 label="C/H2/OneDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=194 label="O2b">]
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=192 label="H_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=203 label="OOC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=192 label="H_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=261 label="C_methyl">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
""",
)

entry(
    index = 100,
    label = "C/H2/OneDeC",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,Cb,CS] u0 {1,S}
5    Cs               u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.024161, 'd13': 0.049558, 'd23': 0.072932},
        uncertainties = {'d12': 0.057279, 'd13': 0.054462, 'd23': 0.074071},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 142 distances.
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=261 label="C_methyl">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=194 label="O2b">]
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=192 label="H_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=203 label="OOC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=192 label="H_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=261 label="C_methyl">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
""",
)

entry(
    index = 101,
    label = "C/H2/CtCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "C/H2/CbCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "C/H2/COCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    CO u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.009947, 'd13': 0.035853, 'd23': 0.028102},
        uncertainties = {'d12': 0.060765, 'd13': 0.031168, 'd23': 0.054265},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 25 distances.
[<Entry index=103 label="C/H2/COCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=261 label="C_methyl">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=192 label="H_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=246 label="CO_rad/OneDe">]
""",
)

entry(
    index = 104,
    label = "C/H2/CO\H/Cs\H3",
    group = 
"""
1     Cs u0 {2,S} {5,S} {6,S} {7,S}
2  *1 C  u0 {1,S} {3,S} {8,S} {9,S}
3     CO u0 {2,S} {4,D} {10,S}
4     O  u0 {3,D}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8  *2 H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.042688, 'd13': 0.051872, 'd23': 0.092647},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
""",
)

entry(
    index = 105,
    label = "C/H2/CdCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cd u0 {1,S} {6,D}
5    Cs u0 {1,S}
6    C  u0 {4,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.031462, 'd13': 0.052492, 'd23': 0.082528},
        uncertainties = {'d12': 0.05744, 'd13': 0.058598, 'd23': 0.078312},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 117 distances.
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=194 label="O2b">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=203 label="OOC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=192 label="H_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=261 label="C_methyl">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
""",
)

entry(
    index = 106,
    label = "C/H2/Cd\H_Cd\H2/Cs\H3",
    group = 
"""
1     Cs u0 {2,S} {5,S} {6,S} {7,S}
2  *1 C  u0 {1,S} {3,S} {8,S} {9,S}
3     Cd u0 {2,S} {4,D} {10,S}
4     C  u0 {3,D} {11,S} {12,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8  *2 H  u0 {2,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {4,S}
12    H  u0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.016956, 'd13': 0.051069, 'd23': 0.066494},
        uncertainties = {'d12': 0.043037, 'd13': 0.051811, 'd23': 0.041284},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 28 distances.
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
""",
)

entry(
    index = 107,
    label = "C/H2/CSCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    CS u0 {1,S} {6,D}
5    Cs u0 {1,S}
6    S  u0 {4,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "C/H2/OneDeO",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             u0 {1,S}
3    H             u0 {1,S}
4    [Cd,Ct,CO,Cb] u0 {1,S}
5    O             u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.051844, 'd13': 0.070328, 'd23': 0.123066},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=108 label="C/H2/OneDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
""",
)

entry(
    index = 109,
    label = "C/H2/OneDeS",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,Cb,CS] u0 {1,S}
5    S                u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "C/H2/CbS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
5    S  u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "C/H2/CtS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
5    S  u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "C/H2/CdS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cd u0 {1,S} {6,D}
5    S  u0 {1,S}
6    C  u0 {4,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "C/H2/CSS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    CS u0 {1,S} {6,D}
5    S  u0 {1,S}
6    S  u0 {4,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "C/H2/TwoDe",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    H                u0 {1,S}
4    [Cd,Ct,CO,Cb,CS] u0 {1,S}
5    [Cd,Ct,CO,Cb,CS] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.050441, 'd13': 0.070842, 'd23': 0.120449},
        uncertainties = {'d12': 0.052215, 'd13': 0.081269, 'd23': 0.090171},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 85 distances.
[<Entry index=127 label="C/H2/CdCd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=192 label="H_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=241 label="Cb_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=203 label="OOC">]
""",
)

entry(
    index = 115,
    label = "C/H2/CtCt",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
5    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "C/H2/CtCb",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
5    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "C/H2/CtCO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
5    CO u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "C/H2/CbCb",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
5    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "C/H2/CbCO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
5    CO u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "C/H2/COCO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    CO u0 {1,S}
5    CO u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "C/H2/CdCt",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cd u0 {1,S} {6,D}
5    Ct u0 {1,S}
6    C  u0 {4,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "C/H2/CtCS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
5    CS u0 {1,S} {6,D}
6    S  u0 {5,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "C/H2/CdCb",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cd u0 {1,S} {6,D}
5    Cb u0 {1,S}
6    C  u0 {4,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "C/H2/CbCS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
5    CS u0 {1,S} {6,D}
6    S  u0 {5,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "C/H2/CdCO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cd u0 {1,S} {6,D}
5    CO u0 {1,S}
6    C  u0 {4,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    label = "C/H2/COCS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    CO u0 {1,S}
5    CS u0 {1,S} {6,D}
6    S  u0 {5,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    label = "C/H2/CdCd",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cd u0 {1,S} {6,D}
5    Cd u0 {1,S} {7,D}
6    C  u0 {4,D}
7    C  u0 {5,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.050441, 'd13': 0.070842, 'd23': 0.120449},
        uncertainties = {'d12': 0.052215, 'd13': 0.081269, 'd23': 0.090171},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 85 distances.
[<Entry index=127 label="C/H2/CdCd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=192 label="H_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=241 label="Cb_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=203 label="OOC">]
""",
)

entry(
    index = 128,
    label = "C/H2/CdCS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    Cd u0 {1,S} {6,D}
5    CS u0 {1,S} {7,D}
6    C  u0 {4,D}
7    S  u0 {5,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    label = "C/H2/CSCS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    CS u0 {1,S} {6,D}
5    CS u0 {1,S} {7,D}
6    S  u0 {4,D}
7    S  u0 {5,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
    label = "C/H2/Cb",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    C  u0 {1,S}
5    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
    label = "C_ter",
    group = 
"""
1 *1 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    R!H u0 {1,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.014844, 'd13': 0.04671, 'd23': 0.062775},
        uncertainties = {'d12': 0.045497, 'd13': 0.073462, 'd23': 0.073291},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 91 distances.
[<Entry index=133 label="C/H/Cs3">, <Entry index=194 label="O2b">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=178 label="C/H/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=198 label="O_pri_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=261 label="C_methyl">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=241 label="Cb_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=192 label="H_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=139 label="C/H/Cs2O">, <Entry index=192 label="H_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
""",
)

entry(
    index = 132,
    label = "C/H/NonDe",
    group = 
"""
1 *1 C          u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H          u0 {1,S}
3    [Cs,O,S,N] u0 {1,S}
4    [Cs,O,S,N] u0 {1,S}
5    [Cs,O,S,N] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.00901, 'd13': 0.012887, 'd23': 0.001875},
        uncertainties = {'d12': 0.059054, 'd13': 0.14504, 'd23': 0.133907},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 16 distances.
[<Entry index=133 label="C/H/Cs3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=194 label="O2b">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=241 label="Cb_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=192 label="H_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=139 label="C/H/Cs2O">, <Entry index=192 label="H_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=203 label="OOC">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=200 label="O_rad/NonDeC">]
""",
)

entry(
    index = 133,
    label = "C/H/Cs3",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.014607, 'd13': 0.020309, 'd23': 0.003765},
        uncertainties = {'d12': 0.059341, 'd13': 0.051509, 'd23': 0.057793},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 15 distances.
[<Entry index=133 label="C/H/Cs3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=194 label="O2b">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=241 label="Cb_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=192 label="H_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=203 label="OOC">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=200 label="O_rad/NonDeC">]
""",
)

entry(
    index = 134,
    label = "C/H/Cs3_5ring",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cs u0 {1,S} {6,S}
4    Cs u0 {1,S} {7,S}
5    Cs u0 {1,S}
6    Cs u0 {3,S} {7,S}
7    Cs u0 {4,S} {6,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "C/H/Cs3_5ring_fused6",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cs u0 {1,S} {6,S}
4    Cs u0 {1,S} {7,S}
5    Cs u0 {1,S} {8,S}
6    Cs u0 {3,S} {7,S}
7    Cs u0 {4,S} {6,S} {8,S}
8    Cs u0 {5,S} {7,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "C/H/Cs3_5ring_adj5",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cs u0 {1,S} {6,S}
4    Cs u0 {1,S} {7,S} {9,S}
5    Cs u0 {1,S} {8,S}
6    Cs u0 {3,S} {7,S}
7    Cs u0 {4,S} {6,S}
8    Cs u0 {5,S} {9,S}
9    Cs u0 {4,S} {8,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "C/H/Cs2/Cs\O",
    group = 
"""
1     Cs u0 {2,S} {6,S} {7,S} {8,S}
2  *1 C  u0 {1,S} {3,S} {5,S} {9,S}
3     Cs u0 {2,S} {4,S} {10,S} {11,S}
4     O  u0 {3,S} {12,S}
5     Cs u0 {2,S} {13,S} {14,S} {15,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {1,S}
9  *2 H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    H  u0 {5,S}
14    H  u0 {5,S}
15    H  u0 {5,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 408,
    label = "C/H/Cs2N",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    N  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "C/H/NDMustO",
    group = 
"""
1 *1 C      u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H      u0 {1,S}
3    O      u0 {1,S}
4    [Cs,O] u0 {1,S}
5    [Cs,O] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.125316, 'd13': -0.165232, 'd23': -0.043488},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=139 label="C/H/Cs2O">, <Entry index=192 label="H_rad">]
""",
)

entry(
    index = 139,
    label = "C/H/Cs2O",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    O  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.125316, 'd13': -0.165232, 'd23': -0.043488},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=139 label="C/H/Cs2O">, <Entry index=192 label="H_rad">]
""",
)

entry(
    index = 140,
    label = "C/H/CsO2",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    O  u0 {1,S}
4    O  u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "C/H/O3",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 {1,S}
3    O u0 {1,S}
4    O u0 {1,S}
5    O u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    label = "C/H/NDMustS",
    group = 
"""
1 *1 C      u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H      u0 {1,S}
3    S      u0 {1,S}
4    [Cs,S] u0 {1,S}
5    [Cs,S] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    label = "C/H/Cs2S",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    S  u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    label = "C/H/CsS2",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    S  u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
    label = "C/H/S3",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 {1,S}
3    S u0 {1,S}
4    S u0 {1,S}
5    S u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    label = "C/H/NDMustOS",
    group = 
"""
1 *1 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H        u0 {1,S}
3    O        u0 {1,S}
4    S        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    label = "C/H/CsOS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    O  u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "C/H/OneDe",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]         u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.018401, 'd13': 0.05201, 'd23': 0.072289},
        uncertainties = {'d12': 0.042706, 'd13': 0.053881, 'd23': 0.057008},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 74 distances.
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=198 label="O_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=261 label="C_methyl">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
""",
)

entry(
    index = 149,
    label = "C/H/Cs2",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cs               u0 {1,S}
5    Cs               u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.018401, 'd13': 0.05201, 'd23': 0.072289},
        uncertainties = {'d12': 0.042706, 'd13': 0.053881, 'd23': 0.057008},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 74 distances.
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=198 label="O_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=261 label="C_methyl">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
""",
)

entry(
    index = 150,
    label = "C/H/Cs2Ct",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 151,
    label = "C/H/Cs2Cb",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 152,
    label = "C/H/Cs2CO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.018401, 'd13': 0.05201, 'd23': 0.072289},
        uncertainties = {'d12': 0.042706, 'd13': 0.053881, 'd23': 0.057008},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 74 distances.
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=198 label="O_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=261 label="C_methyl">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
""",
)

entry(
    index = 153,
    label = "C/H/Cs2Cd",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cd u0 {1,S} {6,D}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    C  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 154,
    label = "C/H/Cs2CS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    CS u0 {1,S} {6,D}
4    Cs u0 {1,S}
5    Cs u0 {1,S}
6    S  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 155,
    label = "C/H/CsO",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    O             u0 {1,S}
5    Cs            u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 156,
    label = "C/H/CsS",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    S                u0 {1,S}
5    Cs               u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "C/H/CbCsS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cb u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "C/H/CtCsS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Ct u0 {1,S}
4    S  u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 159,
    label = "C/H/CdCsS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cd u0 {1,S} {6,D}
4    S  u0 {1,S}
5    Cs u0 {1,S}
6    C  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 160,
    label = "C/H/CSCsS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    CS u0 {1,S} {6,D}
4    S  u0 {1,S}
5    Cs u0 {1,S}
6    S  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 161,
    label = "C/H/OO",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    O             u0 {1,S}
5    O             u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 162,
    label = "C/H/OS",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    O             u0 {1,S}
5    S             u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 163,
    label = "C/H/SS",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    S             u0 {1,S}
5    S             u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 164,
    label = "C/H/TwoDe",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.112601, 'd13': 0.16014, 'd23': 0.269912},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=178 label="C/H/CdCd">, <Entry index=261 label="C_methyl">]
""",
)

entry(
    index = 165,
    label = "C/H/Cs",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    Cs               u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.112601, 'd13': 0.16014, 'd23': 0.269912},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=178 label="C/H/CdCd">, <Entry index=261 label="C_methyl">]
""",
)

entry(
    index = 166,
    label = "C/H/CtCt",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 167,
    label = "C/H/CtCb",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 168,
    label = "C/H/CtCO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Ct u0 {1,S}
4    CO u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 169,
    label = "C/H/CbCb",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 170,
    label = "C/H/CbCO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cb u0 {1,S}
4    CO u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 171,
    label = "C/H/COCO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    CO u0 {1,S}
4    CO u0 {1,S}
5    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 172,
    label = "C/H/CdCt",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cd u0 {1,S} {6,D}
4    Ct u0 {1,S}
5    Cs u0 {1,S}
6    C  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 173,
    label = "C/H/CtCS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Ct u0 {1,S}
4    CS u0 {1,S} {6,D}
5    Cs u0 {1,S}
6    S  u0 {4,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 174,
    label = "C/H/CdCb",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cd u0 {1,S} {6,D}
4    Cb u0 {1,S}
5    Cs u0 {1,S}
6    C  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 175,
    label = "C/H/CbCS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cb u0 {1,S}
4    Cd u0 {1,S} {6,D}
5    Cs u0 {1,S}
6    S  u0 {4,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 176,
    label = "C/H/CdCO",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cd u0 {1,S} {6,D}
4    CO u0 {1,S}
5    Cs u0 {1,S}
6    C  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 177,
    label = "C/H/COCS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    CO u0 {1,S}
4    CS u0 {1,S} {6,D}
5    Cs u0 {1,S}
6    S  u0 {4,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 178,
    label = "C/H/CdCd",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cd u0 {1,S} {6,D}
4    Cd u0 {1,S} {7,D}
5    Cs u0 {1,S}
6    C  u0 {3,D}
7    C  u0 {4,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.112601, 'd13': 0.16014, 'd23': 0.269912},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=178 label="C/H/CdCd">, <Entry index=261 label="C_methyl">]
""",
)

entry(
    index = 179,
    label = "C/H/CdCS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    Cd u0 {1,S} {6,D}
4    CS u0 {1,S} {7,D}
5    Cs u0 {1,S}
6    C  u0 {3,D}
7    S  u0 {4,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 180,
    label = "C/H/CSCS",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    CS u0 {1,S} {6,D}
4    CS u0 {1,S} {7,D}
5    Cs u0 {1,S}
6    S  u0 {3,D}
7    S  u0 {4,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 181,
    label = "C/H/TDMustO",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    O             u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 182,
    label = "C/H/TDMustS",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    S             u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 183,
    label = "C/H/ThreeDe",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
5    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 184,
    label = "C/H/Cb",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    C  u0 {1,S}
4    C  u0 {1,S}
5    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 409,
    label = "N3_H",
    group = 
"""
1 *1 [N3s,N3d] u0 {2,S}
2 *2 H         u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 402,
    label = "N3s_H",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    R   u0 {1,S}
4    R   u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 410,
    label = "NH3",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 411,
    label = "N3s_pri_H",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    R!H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 450,
    label = "N3s/H2/NonDe",
    group = 
"""
1 *1 N3s         u0 {2,S} {3,S} {4,S}
2 *2 H           u0 {1,S}
3    H           u0 {1,S}
4    [N3s,Cs,Os] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 451,
    label = "N3s/H2/NonDeC",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    Cs  u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 452,
    label = "N3s/H2/NonDeO",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    Os  u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 453,
    label = "N3s/H2/NonDeN",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    N3s u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 472,
    label = "N3s/H2/OneDe",
    group = 
"""
1 *1 N3s                       u0 {2,S} {3,S} {4,S}
2 *2 H                         u0 {1,S}
3    H                         u0 {1,S}
4    [Cd,Cdd,Ct,CO,CS,N3d,N5d] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 473,
    label = "N3s/H2/OneDeN",
    group = 
"""
1 *1 N3s       u0 {2,S} {3,S} {4,S}
2 *2 H         u0 {1,S}
3    H         u0 {1,S}
4    [N3d,N5d] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 412,
    label = "N3s_sec_H",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    R!H u0 {1,S}
4    R!H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 413,
    label = "N3d_H",
    group = 
"""
1 *1 N3d u0 {2,S} {3,D}
2 *2 H   u0 {1,S}
3    R!H u0 {1,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 465,
    label = "N3d/H/NonDe",
    group = 
"""
1 *1 N3d         u0 {2,S} {3,D}
2 *2 H           u0 {1,S}
3    [N3d,Od,Cd] u0 {1,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 446,
    label = "N3d/H/NonDeC",
    group = 
"""
1 *1 N3d u0 {2,S} {3,D}
2 *2 H   u0 {1,S}
3    Cd  u0 {1,D} {4,S} {5,S}
4    R   u0 {3,S}
5    R   u0 {3,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 447,
    label = "N3d/H/NonDeO",
    group = 
"""
1 *1 N3d u0 {2,S} {3,D}
2 *2 H   u0 {1,S}
3    Od  u0 {1,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 448,
    label = "N3d/H/NonDeN",
    group = 
"""
1 *1 N3d u0 {2,S} {3,D}
2 *2 H   u0 {1,S}
3    N3d u0 {1,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 466,
    label = "N3d/H/OneDe",
    group = 
"""
1 *1 N3d                   u0 {2,S} {3,D}
2 *2 H                     u0 {1,S}
3    [Cd,Ct,Cb,CO,N5d,N5t] u0 {1,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 467,
    label = "N3d/H/OneDeCO",
    group = 
"""
1 *1 N3d u0 {2,S} {3,D}
2 *2 H   u0 {1,S}
3    CO  u0 {1,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 468,
    label = "N3d/H/OneDeN",
    group = 
"""
1 *1 N3d       u0 {2,S} {3,D}
2 *2 H         u0 {1,S}
3    [N5d,N5t] u0 {1,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 414,
    label = "N5_H",
    group = 
"""
1 *1 [N5s,N5d,N5dd,N5t,N5b] u0 {2,S}
2 *2 H                      u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 415,
    label = "N5d_H",
    group = 
"""
1 *1 N5d u0 {2,S}
2 *2 H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 456,
    label = "N5d/H/NonDeOO",
    group = 
"""
1 *1 N5d u0 {2,S} {3,S} {4,D}
2 *2 H   u0 {1,S}
3    Os  u0 {1,S}
4    Od  u0 {1,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 185,
    label = "Xrad_H",
    group = 
"""
1 *1 R u1 {2,S}
2 *2 H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.087089, 'd13': -0.015089, 'd23': -0.105166},
        uncertainties = {'d12': 0.095837, 'd13': 0.076073, 'd23': 0.075208},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 47 distances.
[<Entry index=443 label="OH_rad_H">, <Entry index=261 label="C_methyl">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=443 label="OH_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=443 label="OH_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=192 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=443 label="OH_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=443 label="OH_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=443 label="OH_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=443 label="OH_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=325 label="C_rad/H/CdCd">]
""",
)

entry(
    index = 469,
    label = "C_rad_H",
    group = 
"""
1 *1 C u1 {2,S}
2 *2 H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.161783, 'd13': 0.046196, 'd23': -0.118691},
        uncertainties = {'d12': 0.09041, 'd13': 0.091701, 'd23': 0.041123},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 31 distances.
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=192 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
""",
)

entry(
    index = 442,
    label = "CH3_rad_H",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.161783, 'd13': 0.046196, 'd23': -0.118691},
        uncertainties = {'d12': 0.09041, 'd13': 0.091701, 'd23': 0.041123},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 31 distances.
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=192 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
""",
)

entry(
    index = 470,
    label = "Cs/H2/OneDeN",
    group = 
"""
1 *1 C         u1 {2,S} {3,S} {4,S}
2 *2 H         u0 {1,S}
3    H         u0 {1,S}
4    [N3d,N5d] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 443,
    label = "OH_rad_H",
    group = 
"""
1 *1 O u1 {2,S}
2 *2 H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.064099, 'd13': -0.139134, 'd23': -0.07779},
        uncertainties = {'d12': 0.117369, 'd13': 0.039756, 'd23': 0.12556},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 16 distances.
[<Entry index=443 label="OH_rad_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=443 label="OH_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=261 label="C_methyl">]
[<Entry index=443 label="OH_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=443 label="OH_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=443 label="OH_rad_H">, <Entry index=273 label="C_rad/H2/O">]
""",
)

entry(
    index = 186,
    label = "Srad_H",
    group = 
"""
1 *1 S u1 {2,S}
2 *2 H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 416,
    label = "N3s_rad_H",
    group = 
"""
1 *1 N3s u1 {2,S}
2 *2 H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 417,
    label = "NH2_rad_H",
    group = 
"""
1 *1 N3s u1 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 418,
    label = "N3s_rad_H_pri",
    group = 
"""
1 *1 N3s     u1 {2,S} {3,S}
2 *2 H       u0 {1,S}
3    [C,N,O] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 449,
    label = "N3s_rad_H/H/NonDeN",
    group = 
"""
1 *1 N3s u1 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    N3s u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 444,
    label = "Xbirad_H",
    group = "OR{CH2_triplet_H, CH2_singlet_H, NH_triplet_H, NH_singlet_H}",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 476,
    label = "CH2_triplet_H",
    group = 
"""
1 *1 Cs u2 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 477,
    label = "CH2_singlet_H",
    group = 
"""
1 *1 C u2 {2,S} {3,S}
2 *2 H u0 {1,S}
3    H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 478,
    label = "NH_triplet_H",
    group = 
"""
1 *1 N u2 {2,S}
2 *2 H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 479,
    label = "NH_singlet_H",
    group = 
"""
1 *1 N u2 {2,S}
2 *2 H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 474,
    label = "Xtrirad_H",
    group = "OR{C_quartet_H, C_doublet_H}",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 480,
    label = "C_quartet_H",
    group = 
"""
1 *1 C u3 {2,S}
2 *2 H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 481,
    label = "C_doublet_H",
    group = 
"""
1 *1 C u3 {2,S}
2 *2 H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 475,
    label = "Y_1centerquadrad",
    group = "OR{C_quintet, C_triplet, C_singlet}",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 482,
    label = "C_quintet",
    group = 
"""
1 *3 C u4
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 483,
    label = "C_triplet",
    group = 
"""
1 *3 C u4
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 484,
    label = "C_singlet",
    group = 
"""
1 *3 C u4
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 419,
    label = "Y_1centertrirad",
    group = "OR{N_atom_quartet, N_atom_doublet, CH_quartet, CH_doublet}",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 485,
    label = "N_atom_quartet",
    group = 
"""
1 *3 N u3
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 486,
    label = "N_atom_doublet",
    group = 
"""
1 *3 N u3
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 487,
    label = "CH_quartet",
    group = 
"""
1 *3 C u3 {2,S}
2    H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 487,
    label = "CH_doublet",
    group = 
"""
1 *3 C u3 {2,S}
2    H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 188,
    label = "Y_1centerbirad",
    group = 
"""
1 *3 [Cs,Cd,CO,CS,O,S,N] u2
""",
    distances = DistanceData(
        distances = {'d12': -0.105924, 'd13': -0.017502, 'd23': 0.085479},
        uncertainties = {'d12': 0.073593, 'd13': 0.073666, 'd23': 0.095589},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 47 distances.
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=72 label="C/H3/O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=190 label="CH2_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=72 label="C/H3/O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=61 label="C_methane">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=42 label="CO_pri">, <Entry index=190 label="CH2_triplet">]
[<Entry index=4 label="H2">, <Entry index=190 label="CH2_triplet">]
""",
)

entry(
    index = 189,
    label = "O_atom_triplet",
    group = 
"""
1 *3 O u2
""",
    distances = DistanceData(
        distances = {'d12': -0.080806, 'd13': -0.140474, 'd23': -0.062319},
        uncertainties = {'d12': 0.121419, 'd13': 0.037579, 'd23': 0.115476},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 16 distances.
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=72 label="C/H3/O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=61 label="C_methane">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=189 label="O_atom_triplet">]
""",
)

entry(
    index = 488,
    label = "O_atom_singlet",
    group = 
"""
1 *3 O u2
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 190,
    label = "CH2_triplet",
    group = 
"""
1 *3 Cs u2 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.118763, 'd13': 0.04535, 'd23': 0.16102},
        uncertainties = {'d12': 0.042205, 'd13': 0.088979, 'd23': 0.091111},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 31 distances.
[<Entry index=9 label="O/H/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=72 label="C/H3/O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=190 label="CH2_triplet">]
[<Entry index=42 label="CO_pri">, <Entry index=190 label="CH2_triplet">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=190 label="CH2_triplet">]
[<Entry index=4 label="H2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=190 label="CH2_triplet">]
""",
)

entry(
    index = 489,
    label = "CH2_singlet",
    group = 
"""
1 *3 Cs u2 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 422,
    label = "NH_triplet",
    group = 
"""
1 *3 N3s u2 {2,s}
2    H   u0 {1,s}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 490,
    label = "NH_singlet",
    group = 
"""
1 *3 N u2 {2,S}
2    H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 191,
    label = "Y_rad",
    group = 
"""
1 *3 R u1
""",
    distances = DistanceData(
        distances = {'d12': 0.003247, 'd13': 0.000536, 'd23': -0.00262},
        uncertainties = {'d12': 0.079468, 'd13': 0.06712, 'd23': 0.077648},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1601 distances.
[<Entry index=47 label="CO/H/OneDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=61 label="C_methane">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=4 label="H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=203 label="OOC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=40 label="Cb_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=192 label="H_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=42 label="CO_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=203 label="OOC">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=4 label="H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=261 label="C_methyl">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=61 label="C_methane">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=13 label="ROOH_sec">, <Entry index=194 label="O2b">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=374 label="C_rad/CdCdCs">]
[<Entry index=4 label="H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=4 label="H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=16 label="Orad_O_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=40 label="Cb_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=203 label="OOC">]
[<Entry index=96 label="C/H2/O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=42 label="CO_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=203 label="OOC">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=232 label="Cd_Cd\H\Cs_rad/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=40 label="Cb_H">, <Entry index=192 label="H_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=4 label="H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=261 label="C_methyl">]
[<Entry index=72 label="C/H3/O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=42 label="CO_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=192 label="H_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=192 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=61 label="C_methane">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=192 label="H_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=443 label="OH_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=194 label="O2b">]
[<Entry index=77 label="C/H3/CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=7 label="O_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=7 label="O_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=198 label="O_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=198 label="O_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=261 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=194 label="O2b">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=16 label="Orad_O_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=4 label="H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=194 label="O2b">]
[<Entry index=42 label="CO_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/O">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=108 label="C/H2/OneDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=192 label="H_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=203 label="OOC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=261 label="C_methyl">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=67 label="C/H3/Cs\H2\Cs|O">, <Entry index=192 label="H_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=7 label="O_pri">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=443 label="OH_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=192 label="H_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=42 label="CO_pri">, <Entry index=192 label="H_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=241 label="Cb_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=42 label="CO_pri">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=61 label="C_methane">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=61 label="C_methane">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=198 label="O_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=198 label="O_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=72 label="C/H3/O">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=139 label="C/H/Cs2O">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H2/Cs\H2\Cs|Cs#O">]
[<Entry index=42 label="CO_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=178 label="C/H/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=306 label="C_rad/H/OneDeO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=192 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=192 label="H_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=203 label="OOC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=241 label="Cb_rad">]
[<Entry index=4 label="H2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=443 label="OH_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=261 label="C_methyl">]
[<Entry index=40 label="Cb_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=61 label="C_methane">, <Entry index=241 label="Cb_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=198 label="O_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=72 label="C/H3/O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=203 label="OOC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=203 label="OOC">]
[<Entry index=61 label="C_methane">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=61 label="C_methane">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=203 label="OOC">]
[<Entry index=72 label="C/H3/O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=61 label="C_methane">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=11 label="H2O2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=335 label="C_rad/Cs2O">]
[<Entry index=7 label="O_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=203 label="OOC">]
[<Entry index=40 label="Cb_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=194 label="O2b">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=7 label="O_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=261 label="C_methyl">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=14 label="ROOH_ter">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=203 label="OOC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=203 label="OOC">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=241 label="Cb_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=40 label="Cb_H">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=198 label="O_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=16 label="Orad_O_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=194 label="O2b">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=61 label="C_methane">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=203 label="OOC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=72 label="C/H3/O">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=203 label="OOC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=192 label="H_rad">]
[<Entry index=61 label="C_methane">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=194 label="O2b">]
[<Entry index=443 label="OH_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=192 label="H_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="Cb_rad">]
[<Entry index=61 label="C_methane">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=454 label="O/H/OneDeC">, <Entry index=192 label="H_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=198 label="O_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=96 label="C/H2/O2">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=491 label="O_rad/OneDeC">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=61 label="C_methane">, <Entry index=192 label="H_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=203 label="OOC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=192 label="H_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=203 label="OOC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=203 label="OOC">]
[<Entry index=16 label="Orad_O_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/O">, <Entry index=194 label="O2b">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=7 label="O_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=40 label="Cb_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=40 label="Cb_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=61 label="C_methane">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
""",
)

entry(
    index = 192,
    label = "H_rad",
    group = 
"""
1 *3 H u1
""",
    distances = DistanceData(
        distances = {'d12': -0.040745, 'd13': -0.371364, 'd23': -0.33348},
        uncertainties = {'d12': 0.108975, 'd13': 0.127315, 'd23': 0.162799},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 64 distances.
[<Entry index=454 label="O/H/OneDeC">, <Entry index=192 label="H_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=192 label="H_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=192 label="H_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=192 label="H_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=192 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=192 label="H_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=192 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=192 label="H_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=192 label="H_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=192 label="H_rad">]
[<Entry index=67 label="C/H3/Cs\H2\Cs|O">, <Entry index=192 label="H_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=192 label="H_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=192 label="H_rad">]
[<Entry index=61 label="C_methane">, <Entry index=192 label="H_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=192 label="H_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=192 label="H_rad">]
[<Entry index=139 label="C/H/Cs2O">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=192 label="H_rad">]
[<Entry index=7 label="O_pri">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=192 label="H_rad">]
""",
)

entry(
    index = 193,
    label = "Y_2centeradjbirad",
    group = 
"""
1 *3 [Ct,Os,Ss] u1 {2,[S,T]}
2    [Ct,Os,Ss] u1 {1,[S,T]}
""",
    distances = DistanceData(
        distances = {'d12': 0.196925, 'd13': -0.051234, 'd23': -0.245407},
        uncertainties = {'d12': 0.185254, 'd13': 0.128488, 'd23': 0.093584},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 18 distances.
[<Entry index=133 label="C/H/Cs3">, <Entry index=194 label="O2b">]
[<Entry index=42 label="CO_pri">, <Entry index=194 label="O2b">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=77 label="C/H3/CO">, <Entry index=194 label="O2b">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=72 label="C/H3/O">, <Entry index=194 label="O2b">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=194 label="O2b">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=194 label="O2b">]
[<Entry index=12 label="ROOH_pri">, <Entry index=194 label="O2b">]
[<Entry index=13 label="ROOH_sec">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=194 label="O2b">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=194 label="O2b">]
""",
)

entry(
    index = 194,
    label = "O2b",
    group = 
"""
1 *3 Os u1 {2,S}
2    Os u1 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.196925, 'd13': -0.051234, 'd23': -0.245407},
        uncertainties = {'d12': 0.185254, 'd13': 0.128488, 'd23': 0.093584},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 18 distances.
[<Entry index=133 label="C/H/Cs3">, <Entry index=194 label="O2b">]
[<Entry index=42 label="CO_pri">, <Entry index=194 label="O2b">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=77 label="C/H3/CO">, <Entry index=194 label="O2b">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=72 label="C/H3/O">, <Entry index=194 label="O2b">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=194 label="O2b">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=194 label="O2b">]
[<Entry index=12 label="ROOH_pri">, <Entry index=194 label="O2b">]
[<Entry index=13 label="ROOH_sec">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=194 label="O2b">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=194 label="O2b">]
""",
)

entry(
    index = 195,
    label = "C2b",
    group = 
"""
1 *3 Ct u1 {2,T}
2    Ct u1 {1,T}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 196,
    label = "Ct_rad",
    group = 
"""
1 *3 C     u1 {2,T}
2    [C,N] u0 {1,T}
""",
    distances = DistanceData(
        distances = {'d12': -0.198406, 'd13': 0.154308, 'd23': 0.408733},
        uncertainties = {'d12': 0.227203, 'd13': 0.295498, 'd23': 0.302513},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 6 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
""",
)

entry(
    index = 423,
    label = "Ct_rad/Ct",
    group = 
"""
1 *3 Ct u1 {2,T}
2    Ct u0 {1,T}
""",
    distances = DistanceData(
        distances = {'d12': -0.198406, 'd13': 0.154308, 'd23': 0.408733},
        uncertainties = {'d12': 0.227203, 'd13': 0.295498, 'd23': 0.302513},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 6 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
""",
)

entry(
    index = 424,
    label = "Ct_rad/N",
    group = 
"""
1 *3 Ct        u1 {2,T}
2    [N3t,N5t] u0 {1,T}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 197,
    label = "O_rad",
    group = 
"""
1 *3 O u1 {2,S}
2    R u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.04467, 'd13': -0.143227, 'd23': -0.093882},
        uncertainties = {'d12': 0.104801, 'd13': 0.082472, 'd23': 0.105626},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 171 distances.
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=198 label="O_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=198 label="O_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=198 label="O_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=203 label="OOC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=203 label="OOC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=203 label="OOC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=42 label="CO_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=61 label="C_methane">, <Entry index=203 label="OOC">]
[<Entry index=42 label="CO_pri">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=203 label="OOC">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=40 label="Cb_H">, <Entry index=203 label="OOC">]
[<Entry index=72 label="C/H3/O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=203 label="OOC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=203 label="OOC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=198 label="O_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=203 label="OOC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=42 label="CO_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=491 label="O_rad/OneDeC">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=203 label="OOC">]
[<Entry index=4 label="H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=203 label="OOC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=203 label="OOC">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=203 label="OOC">]
[<Entry index=61 label="C_methane">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=203 label="OOC">]
[<Entry index=16 label="Orad_O_H">, <Entry index=203 label="OOC">]
[<Entry index=40 label="Cb_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=203 label="OOC">]
[<Entry index=7 label="O_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=198 label="O_pri_rad">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=203 label="OOC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=198 label="O_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=203 label="OOC">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=40 label="Cb_H">, <Entry index=198 label="O_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=200 label="O_rad/NonDeC">]
""",
)

entry(
    index = 198,
    label = "O_pri_rad",
    group = 
"""
1 *3 O u1 {2,S}
2    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.197772, 'd13': -0.131535, 'd23': 0.095937},
        uncertainties = {'d12': 0.068254, 'd13': 0.155623, 'd23': 0.168035},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 13 distances.
[<Entry index=38 label="Cd/H/Cd">, <Entry index=198 label="O_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=198 label="O_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=198 label="O_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=198 label="O_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=198 label="O_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=198 label="O_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=198 label="O_pri_rad">]
""",
)

entry(
    index = 199,
    label = "O_sec_rad",
    group = 
"""
1 *3 O   u1 {2,S}
2    R!H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.032676, 'd13': -0.144143, 'd23': -0.108753},
        uncertainties = {'d12': 0.10777, 'd13': 0.076501, 'd23': 0.101594},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 158 distances.
[<Entry index=63 label="C/H3/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=203 label="OOC">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=203 label="OOC">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=203 label="OOC">]
[<Entry index=16 label="Orad_O_H">, <Entry index=203 label="OOC">]
[<Entry index=40 label="Cb_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=72 label="C/H3/O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=203 label="OOC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=203 label="OOC">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=7 label="O_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=42 label="CO_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=40 label="Cb_H">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=203 label="OOC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=203 label="OOC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=7 label="O_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=42 label="CO_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=203 label="OOC">]
[<Entry index=4 label="H2">, <Entry index=203 label="OOC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=4 label="H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=203 label="OOC">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=203 label="OOC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=203 label="OOC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=203 label="OOC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=203 label="OOC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=72 label="C/H3/O">, <Entry index=203 label="OOC">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=61 label="C_methane">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=203 label="OOC">]
[<Entry index=42 label="CO_pri">, <Entry index=203 label="OOC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=4 label="H2">, <Entry index=491 label="O_rad/OneDeC">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=200 label="O_rad/NonDeC">]
""",
)

entry(
    index = 200,
    label = "O_rad/NonDeC",
    group = 
"""
1 *3 O  u1 {2,S}
2    Cs u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.097731, 'd13': -0.15298, 'd23': -0.050576},
        uncertainties = {'d12': 0.051788, 'd13': 0.072452, 'd23': 0.075727},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 44 distances.
[<Entry index=63 label="C/H3/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=42 label="CO_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=200 label="O_rad/NonDeC">]
""",
)

entry(
    index = 201,
    label = "O_rad/Cs\H2\Cs|H|Cs2",
    group = 
"""
1     C  u0 {2,S} {6,S} {7,S} {8,S}
2     C  u0 {1,S} {3,S} {5,S} {9,S}
3     Cs u0 {2,S} {4,S} {10,S} {11,S}
4  *3 O  u1 {3,S}
5     C  u0 {2,S} {12,S} {13,S} {14,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {1,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {5,S}
13    H  u0 {5,S}
14    H  u0 {5,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 202,
    label = "O_rad/NonDeO",
    group = 
"""
1 *3 O u1 {2,S}
2    O u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.006626, 'd13': -0.139552, 'd23': -0.130986},
        uncertainties = {'d12': 0.117029, 'd13': 0.06464, 'd23': 0.111377},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 113 distances.
[<Entry index=133 label="C/H/Cs3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=203 label="OOC">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=203 label="OOC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=203 label="OOC">]
[<Entry index=16 label="Orad_O_H">, <Entry index=203 label="OOC">]
[<Entry index=40 label="Cb_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=203 label="OOC">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=7 label="O_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=203 label="OOC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=203 label="OOC">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=203 label="OOC">]
[<Entry index=72 label="C/H3/O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=42 label="CO_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=203 label="OOC">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=11 label="H2O2">, <Entry index=203 label="OOC">]
[<Entry index=4 label="H2">, <Entry index=203 label="OOC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=4 label="H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=203 label="OOC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=203 label="OOC">]
[<Entry index=40 label="Cb_H">, <Entry index=203 label="OOC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=203 label="OOC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=72 label="C/H3/O">, <Entry index=203 label="OOC">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=61 label="C_methane">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=42 label="CO_pri">, <Entry index=203 label="OOC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=203 label="OOC">]
""",
)

entry(
    index = 203,
    label = "OOC",
    group = 
"""
1 *3 O u1 {2,S}
2    O u0 {1,S} {3,S}
3    C u0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.01803, 'd13': -0.139325, 'd23': -0.119389},
        uncertainties = {'d12': 0.115455, 'd13': 0.06426, 'd23': 0.122351},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 82 distances.
[<Entry index=78 label="C/H3/Cd">, <Entry index=203 label="OOC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=203 label="OOC">]
[<Entry index=16 label="Orad_O_H">, <Entry index=203 label="OOC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=203 label="OOC">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=203 label="OOC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=203 label="OOC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=203 label="OOC">]
[<Entry index=61 label="C_methane">, <Entry index=203 label="OOC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=203 label="OOC">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=203 label="OOC">]
[<Entry index=4 label="H2">, <Entry index=203 label="OOC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=203 label="OOC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=203 label="OOC">]
[<Entry index=40 label="Cb_H">, <Entry index=203 label="OOC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=72 label="C/H3/O">, <Entry index=203 label="OOC">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=42 label="CO_pri">, <Entry index=203 label="OOC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=203 label="OOC">]
""",
)

entry(
    index = 425,
    label = "O_rad/NonDeN",
    group = 
"""
1 *3 O   u1 {2,S}
2    N3s u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 204,
    label = "O_rad/OneDe",
    group = 
"""
1 *3 O                        u1 {2,S}
2    [Cd,Ct,Cb,CO,CS,N3d,N5d] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.133975, 'd13': -0.375863, 'd23': -0.238186},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=491 label="O_rad/OneDeC">]
""",
)

entry(
    index = 491,
    label = "O_rad/OneDeC",
    group = 
"""
1 *3 O             u1 {2,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.133975, 'd13': -0.375863, 'd23': -0.238186},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=491 label="O_rad/OneDeC">]
""",
)

entry(
    index = 205,
    label = "O_rad/Cd",
    group = 
"""
1 *3 O        u1 {2,S}
2    Cd       u0 {1,S} {3,D}
3    [Cd,Cdd] u0 {2,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 206,
    label = "O_rad/Cd\H_Cd\H2",
    group = 
"""
1 *3 O  u1 {2,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {5,S} {6,S}
4    H  u0 {2,S}
5    H  u0 {3,S}
6    H  u0 {3,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 207,
    label = "O_rad/Cd\H_Cd\H\Cs",
    group = 
"""
1 *3 O  u1 {2,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {5,S} {6,S}
4    H  u0 {2,S}
5    Cs u0 {3,S}
6    H  u0 {3,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 208,
    label = "O_rad/Cd\H_Cd\Cs2",
    group = 
"""
1 *3 O  u1 {2,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {5,S} {6,S}
4    H  u0 {2,S}
5    Cs u0 {3,S}
6    Cs u0 {3,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 209,
    label = "O_rad/Cd\Cs_Cd\H2",
    group = 
"""
1 *3 O  u1 {2,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {5,S} {6,S}
4    Cs u0 {2,S}
5    H  u0 {3,S}
6    H  u0 {3,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 210,
    label = "O_rad/Cd\Cs_Cd\H\Cs",
    group = 
"""
1 *3 O  u1 {2,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {5,S} {6,S}
4    Cs u0 {2,S}
5    Cs u0 {3,S}
6    H  u0 {3,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 211,
    label = "O_rad/Cd\Cs_Cd\Cs2",
    group = 
"""
1 *3 O  u1 {2,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {5,S} {6,S}
4    Cs u0 {2,S}
5    Cs u0 {3,S}
6    Cs u0 {3,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 403,
    label = "InChI=1S/NO3/c2-1(3)4",
    group = 
"""
1 *3 Os  u1 {2,S}
2    N5d u0 {1,S} {3,D} {4,S}
3    Od  u0 {2,D}
4    Os  u0 {2,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 426,
    label = "O_rad/OneDeN",
    group = 
"""
1 *3 O         u1 {2,S}
2    [N3d,N5d] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 212,
    label = "S_rad",
    group = 
"""
1 *3 S u1 {2,S}
2    R u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 213,
    label = "S_pri_rad",
    group = 
"""
1 *3 S u1 {2,S}
2    H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 214,
    label = "S_sec_rad",
    group = 
"""
1 *3 S   u1 {2,S}
2    R!H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 215,
    label = "S_rad/NonDeC",
    group = 
"""
1 *3 S  u1 {2,S}
2    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 216,
    label = "S_rad/NonDeS",
    group = 
"""
1 *3 S u1 {2,S}
2    S u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 217,
    label = "S_rad/OneDe",
    group = 
"""
1 *3 S                u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 218,
    label = "S_rad/Ct",
    group = 
"""
1 *3 S  u1 {2,S}
2    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 219,
    label = "S_rad/Cb",
    group = 
"""
1 *3 S  u1 {2,S}
2    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 220,
    label = "S_rad/CO",
    group = 
"""
1 *3 S  u1 {2,S}
2    CO u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 221,
    label = "S_rad/Cd",
    group = 
"""
1 *3 S  u1 {2,S}
2    Cd u0 {1,S} {3,D}
3    C  u0 {2,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 222,
    label = "S_rad/CS",
    group = 
"""
1 *3 S  u1 {2,S}
2    CS u0 {1,S} {3,D}
3    S  u0 {2,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 223,
    label = "Cd_rad",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    C u0 {1,D}
3    R u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.073729, 'd13': 0.012793, 'd23': 0.085786},
        uncertainties = {'d12': 0.104602, 'd13': 0.091709, 'd23': 0.121493},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 148 distances.
[<Entry index=4 label="H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=4 label="H2">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=4 label="H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=443 label="OH_rad_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=443 label="OH_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=232 label="Cd_Cd\H\Cs_rad/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
""",
)

entry(
    index = 224,
    label = "Cd_pri_rad",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    C u0 {1,D}
3    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.069002, 'd13': 0.014699, 'd23': 0.083311},
        uncertainties = {'d12': 0.099325, 'd13': 0.077924, 'd23': 0.119174},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 125 distances.
[<Entry index=4 label="H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=443 label="OH_rad_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
""",
)

entry(
    index = 225,
    label = "Cd_Cd\H2_pri_rad",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    C u0 {1,D} {4,S} {5,S}
3    H u0 {1,S}
4    H u0 {2,S}
5    H u0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.098768, 'd13': 0.024783, 'd23': 0.120145},
        uncertainties = {'d12': 0.057908, 'd13': 0.074588, 'd23': 0.071644},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 27 distances.
[<Entry index=4 label="H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
""",
)

entry(
    index = 226,
    label = "Cd_Cd\H\Cs_pri_rad",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D} {4,S} {5,S}
3    H  u0 {1,S}
4    Cs u0 {2,S}
5    H  u0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.095921, 'd13': 0.035823, 'd23': 0.129564},
        uncertainties = {'d12': 0.065103, 'd13': 0.068916, 'd23': 0.089319},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 17 distances.
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
""",
)

entry(
    index = 227,
    label = "Cd_Cd\H\Cs|H2|Cs_pri_rad",
    group = 
"""
1    C  u0 {2,S}
2    Cs u0 {1,S} {3,S} {5,S} {6,S}
3    C  u0 {2,S} {4,D} {7,S}
4 *3 C  u1 {3,D} {8,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    H  u0 {3,S}
8    H  u0 {4,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 228,
    label = "Cd_Cd\Cs2_pri_rad",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D} {4,S} {5,S}
3    H  u0 {1,S}
4    Cs u0 {2,S}
5    Cs u0 {2,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 229,
    label = "Cd_sec_rad",
    group = 
"""
1 *3 C   u1 {2,D} {3,S}
2    C   u0 {1,D}
3    R!H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.104143, 'd13': 0.000529, 'd23': 0.101709},
        uncertainties = {'d12': 0.139517, 'd13': 0.155929, 'd23': 0.14398},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 23 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=4 label="H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=4 label="H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=443 label="OH_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=232 label="Cd_Cd\H\Cs_rad/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=7 label="O_pri">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
""",
)

entry(
    index = 230,
    label = "Cd_rad/NonDeC",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3    Cs u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.183902, 'd13': -0.048003, 'd23': 0.132486},
        uncertainties = {'d12': 0.431013, 'd13': 0.473742, 'd23': 0.066715},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 4 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=4 label="H2">, <Entry index=232 label="Cd_Cd\H\Cs_rad/Cs">]
[<Entry index=4 label="H2">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
""",
)

entry(
    index = 231,
    label = "Cd_Cd\H2_rad/Cs",
    group = 
"""
1    C  u0 {2,D} {4,S} {5,S}
2 *3 C  u1 {1,D} {3,S}
3    Cs u0 {2,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.151968, 'd13': -0.008547, 'd23': 0.140026},
        uncertainties = {'d12': 0.249457, 'd13': 0.229094, 'd23': 0.067217},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=4 label="H2">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
""",
)

entry(
    index = 232,
    label = "Cd_Cd\H\Cs_rad/Cs",
    group = 
"""
1    Cs u0 {2,S} {5,S} {6,S} {7,S}
2 *3 C  u1 {1,S} {3,D}
3    C  u0 {2,D} {4,S} {8,S}
4    Cs u0 {3,S}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {1,S}
8    H  u0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.332926, 'd13': -0.232131, 'd23': 0.097304},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=232 label="Cd_Cd\H\Cs_rad/Cs">]
""",
)

entry(
    index = 233,
    label = "Cd_rad/NonDeO",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    C u0 {1,D}
3    O u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 234,
    label = "Cd_rad/NonDeS",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    C u0 {1,D}
3    S u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 427,
    label = "Cd_rad/NonDeN",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    C u0 {1,D}
3    N u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 235,
    label = "Cd_rad/OneDe",
    group = 
"""
1 *3 C                u1 {2,D} {3,S}
2    C                u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.088558, 'd13': 0.010012, 'd23': 0.095695},
        uncertainties = {'d12': 0.104506, 'd13': 0.119145, 'd23': 0.160247},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 19 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=7 label="O_pri">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
""",
)

entry(
    index = 236,
    label = "Cd_rad/Ct",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3    Ct u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.04195, 'd13': -0.061099, 'd23': -0.021111},
        uncertainties = {'d12': 0.177476, 'd13': 0.279251, 'd23': 0.153083},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=4 label="H2">, <Entry index=236 label="Cd_rad/Ct">]
""",
)

entry(
    index = 237,
    label = "Cd_rad/Cb",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 238,
    label = "Cd_rad/CO",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3    CO u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 239,
    label = "Cd_rad/Cd",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3    Cd u0 {1,S} {4,D}
4    C  u0 {3,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.096745, 'd13': 0.022505, 'd23': 0.116215},
        uncertainties = {'d12': 0.111619, 'd13': 0.122399, 'd23': 0.175926},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 16 distances.
[<Entry index=9 label="O/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=7 label="O_pri">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
""",
)

entry(
    index = 240,
    label = "Cd_rad/CS",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3    CS u0 {1,S} {4,D}
4    S  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 241,
    label = "Cb_rad",
    group = 
"""
1 *3 Cb       u1 {2,B} {3,B}
2    [Cb,Cbf] u0 {1,B}
3    [Cb,Cbf] u0 {1,B}
""",
    distances = DistanceData(
        distances = {'d12': -0.088417, 'd13': 0.031776, 'd23': 0.120854},
        uncertainties = {'d12': 0.083816, 'd13': 0.095983, 'd23': 0.107255},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 29 distances.
[<Entry index=78 label="C/H3/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=241 label="Cb_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=61 label="C_methane">, <Entry index=241 label="Cb_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=241 label="Cb_rad">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=241 label="Cb_rad">]
[<Entry index=4 label="H2">, <Entry index=241 label="Cb_rad">]
[<Entry index=7 label="O_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=241 label="Cb_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=241 label="Cb_rad">]
""",
)

entry(
    index = 242,
    label = "CO_rad",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    O u0 {1,D}
3    R u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.049272, 'd13': 0.059738, 'd23': 0.0114},
        uncertainties = {'d12': 0.081192, 'd13': 0.049505, 'd23': 0.055661},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 129 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=61 label="C_methane">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=243 label="CO_pri_rad">]
""",
)

entry(
    index = 243,
    label = "CO_pri_rad",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    O u0 {1,D}
3    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.038355, 'd13': 0.051657, 'd23': 0.012792},
        uncertainties = {'d12': 0.078324, 'd13': 0.045967, 'd23': 0.057969},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 41 distances.
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=243 label="CO_pri_rad">]
""",
)

entry(
    index = 244,
    label = "CO_sec_rad",
    group = 
"""
1 *3 C   u1 {2,D} {3,S}
2    O   u0 {1,D}
3    R!H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.054352, 'd13': 0.063498, 'd23': 0.010752},
        uncertainties = {'d12': 0.084015, 'd13': 0.05195, 'd23': 0.055725},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 88 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=42 label="CO_pri">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=61 label="C_methane">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=61 label="C_methane">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=246 label="CO_rad/OneDe">]
""",
)

entry(
    index = 245,
    label = "CO_rad/NonDe",
    group = 
"""
1 *3 C        u1 {2,D} {3,S}
2    O        u0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.064371, 'd13': 0.067403, 'd23': 0.00329},
        uncertainties = {'d12': 0.098308, 'd13': 0.057595, 'd23': 0.055269},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 54 distances.
[<Entry index=103 label="C/H2/COCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=42 label="CO_pri">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=4 label="H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=61 label="C_methane">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=245 label="CO_rad/NonDe">]
""",
)

entry(
    index = 246,
    label = "CO_rad/OneDe",
    group = 
"""
1 *3 C             u1 {2,D} {3,S}
2    O             u0 {1,D}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.03957, 'd13': 0.057735, 'd23': 0.021762},
        uncertainties = {'d12': 0.059394, 'd13': 0.044424, 'd23': 0.059412},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 34 distances.
[<Entry index=63 label="C/H3/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=61 label="C_methane">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=246 label="CO_rad/OneDe">]
""",
)

entry(
    index = 247,
    label = "CS_rad",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    S u0 {1,D}
3    R u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 248,
    label = "CS_pri_rad",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    S u0 {1,D}
3    H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 249,
    label = "CS_sec_rad",
    group = 
"""
1 *3 C   u1 {2,D} {3,S}
2    S   u0 {1,D}
3    R!H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 250,
    label = "CS_rad/NonDe",
    group = 
"""
1 *3 C        u1 {2,D} {3,S}
2    S        u0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 251,
    label = "CS_rad/Cs",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    S  u0 {1,D}
3    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 252,
    label = "CS_rad/O",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    S u0 {1,D}
3    O u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 253,
    label = "CS_rad/S",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    S u0 {1,D}
3    S u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 254,
    label = "CS_rad/OneDe",
    group = 
"""
1 *3 C                u1 {2,D} {3,S}
2    S                u0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 255,
    label = "CS_rad/Ct",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    S  u0 {1,D}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 256,
    label = "CS_rad/Cb",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    S  u0 {1,D}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 257,
    label = "CS_rad/CO",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    S  u0 {1,D}
3    CO u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 258,
    label = "CS_rad/Cd",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    S  u0 {1,D}
3    Cd u0 {1,S} {4,D}
4    C  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 259,
    label = "CS_rad/CS",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    S  u0 {1,D}
3    CS u0 {1,S} {4,D}
4    S  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 260,
    label = "Cs_rad",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    R u0 {1,S}
3    R u0 {1,S}
4    R u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.018084, 'd13': 0.036995, 'd23': 0.018066},
        uncertainties = {'d12': 0.064419, 'd13': 0.052251, 'd23': 0.053392},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1036 distances.
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=61 label="C_methane">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=4 label="H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=7 label="O_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=261 label="C_methyl">]
[<Entry index=42 label="CO_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=61 label="C_methane">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=61 label="C_methane">, <Entry index=374 label="C_rad/CdCdCs">]
[<Entry index=4 label="H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=40 label="Cb_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=96 label="C/H2/O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=61 label="C_methane">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=261 label="C_methyl">]
[<Entry index=77 label="C/H3/CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=42 label="CO_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=443 label="OH_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=42 label="CO_pri">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=4 label="H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=61 label="C_methane">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=42 label="CO_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=61 label="C_methane">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=261 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=72 label="C/H3/O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=42 label="CO_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=108 label="C/H2/OneDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/O">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=261 label="C_methyl">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=61 label="C_methane">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=443 label="OH_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=42 label="CO_pri">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=40 label="Cb_H">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=40 label="Cb_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H2/Cs\H2\Cs|Cs#O">]
[<Entry index=42 label="CO_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=178 label="C/H/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=11 label="H2O2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=306 label="C_rad/H/OneDeO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=4 label="H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=61 label="C_methane">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=4 label="H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=61 label="C_methane">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=11 label="H2O2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=335 label="C_rad/Cs2O">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=261 label="C_methyl">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=14 label="ROOH_ter">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=40 label="Cb_H">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/O">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=443 label="OH_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=61 label="C_methane">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=443 label="OH_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=42 label="CO_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=261 label="C_methyl">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=96 label="C/H2/O2">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=16 label="Orad_O_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=261 label="C_methyl">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=40 label="Cb_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=40 label="Cb_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=40 label="Cb_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
""",
)

entry(
    index = 261,
    label = "C_methyl",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.054971, 'd13': 0.033416, 'd23': 0.084657},
        uncertainties = {'d12': 0.04465, 'd13': 0.037258, 'd23': 0.062531},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 69 distances.
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=443 label="OH_rad_H">, <Entry index=261 label="C_methyl">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=261 label="C_methyl">]
[<Entry index=96 label="C/H2/O2">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=261 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=261 label="C_methyl">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=178 label="C/H/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=261 label="C_methyl">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=14 label="ROOH_ter">, <Entry index=261 label="C_methyl">]
[<Entry index=42 label="CO_pri">, <Entry index=261 label="C_methyl">]
[<Entry index=72 label="C/H3/O">, <Entry index=261 label="C_methyl">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=261 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=261 label="C_methyl">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=261 label="C_methyl">]
[<Entry index=40 label="Cb_H">, <Entry index=261 label="C_methyl">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=77 label="C/H3/CO">, <Entry index=261 label="C_methyl">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O_pri">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=261 label="C_methyl">]
""",
)

entry(
    index = 262,
    label = "C_pri_rad",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    H   u0 {1,S}
4    R!H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.006814, 'd13': 0.029598, 'd23': 0.035092},
        uncertainties = {'d12': 0.056439, 'd13': 0.045955, 'd23': 0.052104},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 543 distances.
[<Entry index=127 label="C/H2/CdCd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=40 label="Cb_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=7 label="O_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=61 label="C_methane">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=4 label="H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=443 label="OH_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=4 label="H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H2/Cs\H2\Cs|Cs#O">]
[<Entry index=11 label="H2O2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=16 label="Orad_O_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=42 label="CO_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=61 label="C_methane">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=40 label="Cb_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=443 label="OH_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=40 label="Cb_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=96 label="C/H2/O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=443 label="OH_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=61 label="C_methane">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=61 label="C_methane">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=108 label="C/H2/OneDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=61 label="C_methane">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=72 label="C/H3/O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=61 label="C_methane">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=72 label="C/H3/O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=61 label="C_methane">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=61 label="C_methane">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=72 label="C/H3/O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=61 label="C_methane">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=272 label="C_rad/H2/CO">]
""",
)

entry(
    index = 263,
    label = "C_rad/H2/Cs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.037934, 'd13': 0.02626, 'd23': 0.061379},
        uncertainties = {'d12': 0.055797, 'd13': 0.049928, 'd23': 0.049566},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 277 distances.
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=4 label="H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H2/Cs\H2\Cs|Cs#O">]
[<Entry index=11 label="H2O2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=72 label="C/H3/O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=40 label="Cb_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=40 label="Cb_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=4 label="H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=96 label="C/H2/O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=108 label="C/H2/OneDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=61 label="C_methane">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=61 label="C_methane">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=61 label="C_methane">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
""",
)

entry(
    index = 264,
    label = "C_rad/H2/Cs\H3",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cs u0 {1,S} {5,S} {6,S} {7,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
7    H  u0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.029255, 'd13': 0.032056, 'd23': 0.057901},
        uncertainties = {'d12': 0.052402, 'd13': 0.038272, 'd23': 0.057799},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 57 distances.
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=40 label="Cb_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=108 label="C/H2/OneDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=96 label="C/H2/O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=61 label="C_methane">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
""",
)

entry(
    index = 265,
    label = "C_rad/H2/Cs\Cs2\O",
    group = 
"""
1 *3 C  u1 {2,S} {6,S} {7,S}
2    Cs u0 {1,S} {3,S} {4,S} {5,S}
3    C  u0 {2,S}
4    O  u0 {2,S}
5    C  u0 {2,S}
6    H  u0 {1,S}
7    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.123847, 'd13': -0.090402, 'd23': 0.030365},
        uncertainties = {'d12': 1.07071, 'd13': 1.7329, 'd23': 0.738007},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=61 label="C_methane">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
""",
)

entry(
    index = 266,
    label = "C_rad/H2/Cs\H\Cs\Cs|O",
    group = 
"""
1 *3 C  u1 {2,S} {6,S} {7,S}
2    Cs u0 {1,S} {3,S} {5,S} {8,S}
3    C  u0 {2,S} {4,S}
4    O  u0 {3,S}
5    C  u0 {2,S}
6    H  u0 {1,S}
7    H  u0 {1,S}
8    H  u0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.03239, 'd13': 0.034913, 'd23': 0.065607},
        uncertainties = {'d12': 0.06478, 'd13': 0.050022, 'd23': 0.048469},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 24 distances.
[<Entry index=78 label="C/H3/Cd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=40 label="Cb_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=61 label="C_methane">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=4 label="H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=72 label="C/H3/O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=42 label="CO_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
""",
)

entry(
    index = 267,
    label = "C_rad/H2/Cs\H\Cs|Cs\O",
    group = 
"""
1 *3 C  u1 {2,S} {6,S} {7,S}
2    Cs u0 {1,S} {3,S} {4,S} {8,S}
3    C  u0 {2,S} {5,S}
4    O  u0 {2,S}
5    C  u0 {3,S}
6    H  u0 {1,S}
7    H  u0 {1,S}
8    H  u0 {2,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 268,
    label = "C_rad/H2/Cs\H2\Cs|Cs|O",
    group = 
"""
1 *3 C  u1 {2,S} {6,S} {7,S}
2    Cs u0 {1,S} {3,S} {8,S} {9,S}
3    C  u0 {2,S} {4,S} {5,S}
4    C  u0 {3,S}
5    O  u0 {3,S}
6    H  u0 {1,S}
7    H  u0 {1,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 269,
    label = "C_rad/H2/Cs\H2\Cs|Cs#O",
    group = 
"""
1 *3 C  u1 {2,S} {6,S} {7,S}
2    Cs u0 {1,S} {3,S} {8,S} {9,S}
3    C  u0 {2,S} {4,S}
4    C  u0 {3,S} {5,S}
5    O  u0 {4,S}
6    H  u0 {1,S}
7    H  u0 {1,S}
8    H  u0 {2,S}
9    H  u0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.290989, 'd13': -0.249115, 'd23': 0.03848},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H2/Cs\H2\Cs|Cs#O">]
""",
)

entry(
    index = 270,
    label = "C_rad/H2/Ct",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.015214, 'd13': 0.027581, 'd23': 0.00927},
        uncertainties = {'d12': 0.052594, 'd13': 0.030145, 'd23': 0.049175},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 27 distances.
[<Entry index=9 label="O/H/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=4 label="H2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=72 label="C/H3/O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=270 label="C_rad/H2/Ct">]
""",
)

entry(
    index = 271,
    label = "C_rad/H2/Cb",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 272,
    label = "C_rad/H2/CO",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    CO u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.008091, 'd13': 0.020251, 'd23': 0.030305},
        uncertainties = {'d12': 0.04328, 'd13': 0.037519, 'd23': 0.057908},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 63 distances.
[<Entry index=10 label="O/H/NonDeO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=42 label="CO_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=443 label="OH_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=16 label="Orad_O_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=61 label="C_methane">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=272 label="C_rad/H2/CO">]
""",
)

entry(
    index = 273,
    label = "C_rad/H2/O",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    O u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.00167, 'd13': 0.026068, 'd23': 0.031229},
        uncertainties = {'d12': 0.05465, 'd13': 0.035134, 'd23': 0.050966},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 48 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=40 label="Cb_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=4 label="H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=61 label="C_methane">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=443 label="OH_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=273 label="C_rad/H2/O">]
""",
)

entry(
    index = 274,
    label = "C_rad/H2/S",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    S u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 275,
    label = "C_rad/H2/Cd",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    C u0 {1,S} {5,D}
5    C u0 {4,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.050403, 'd13': 0.042623, 'd23': -0.010059},
        uncertainties = {'d12': 0.066846, 'd13': 0.04883, 'd23': 0.058048},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 128 distances.
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=61 label="C_methane">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=61 label="C_methane">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=11 label="H2O2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=72 label="C/H3/O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=61 label="C_methane">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
""",
)

entry(
    index = 276,
    label = "C_rad/H2/Cd\H_Cd\H2",
    group = 
"""
1 *3 C u1 {2,S} {4,S} {5,S}
2    C u0 {1,S} {3,D} {6,S}
3    C u0 {2,D}
4    H u0 {1,S}
5    H u0 {1,S}
6    H u0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.053173, 'd13': 0.043788, 'd23': -0.01152},
        uncertainties = {'d12': 0.072247, 'd13': 0.050939, 'd23': 0.063002},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 100 distances.
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=61 label="C_methane">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=11 label="H2O2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=72 label="C/H3/O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
""",
)

entry(
    index = 277,
    label = "C_rad/H2/Cd\Cs_Cd\H2",
    group = 
"""
1     C u0 {2,D} {5,S} {6,S}
2     C u0 {1,D} {3,S} {4,S}
3  *3 C u1 {2,S} {7,S} {8,S}
4     C u0 {2,S} {9,S} {10,S} {11,S}
5     H u0 {1,S}
6     H u0 {1,S}
7     H u0 {3,S}
8     H u0 {3,S}
9     H u0 {4,S}
10    H u0 {4,S}
11    H u0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.029707, 'd13': 0.015537, 'd23': -0.018702},
        uncertainties = {'d12': 0.110861, 'd13': 0.186899, 'd23': 0.092766},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=9 label="O/H/NonDeC">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=61 label="C_methane">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
""",
)

entry(
    index = 278,
    label = "C_rad/H2/CS",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    C u0 {1,S} {5,D}
5    S u0 {4,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 428,
    label = "C_rad/H2/N",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    N u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 279,
    label = "C_sec_rad",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    R!H u0 {1,S}
4    R!H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.061087, 'd13': 0.04687, 'd23': -0.014298},
        uncertainties = {'d12': 0.077483, 'd13': 0.058291, 'd23': 0.056088},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 333 distances.
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=306 label="C_rad/H/OneDeO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=61 label="C_methane">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=40 label="Cb_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=61 label="C_methane">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=11 label="H2O2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=61 label="C_methane">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=42 label="CO_pri">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=16 label="Orad_O_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=61 label="C_methane">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=40 label="Cb_H">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=40 label="Cb_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
""",
)

entry(
    index = 280,
    label = "C_rad/H/NonDeC",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.026226, 'd13': 0.014344, 'd23': 0.037383},
        uncertainties = {'d12': 0.056348, 'd13': 0.033154, 'd23': 0.060164},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 62 distances.
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=61 label="C_methane">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=40 label="Cb_H">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=443 label="OH_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=16 label="Orad_O_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
""",
)

entry(
    index = 281,
    label = "C_rad/H/NonDeC_5ring_fused6_1",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs u0 {1,S} {5,S} {7,S}
4    Cs u0 {1,S} {6,S}
5    Cs u0 {3,S} {6,S}
6    Cs u0 {4,S} {5,S} {8,S}
7    Cs u0 {3,S} {8,S}
8    Cs u0 {6,S} {7,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 282,
    label = "C_rad/H/NonDeC_5ring_fused6_2",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs u0 {1,S} {5,S} {7,S}
4    Cs u0 {1,S} {6,S} {8,S}
5    Cs u0 {3,S} {6,S}
6    Cs u0 {4,S} {5,S}
7    Cs u0 {3,S} {8,S}
8    Cs u0 {4,S} {7,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 283,
    label = "C_rad/H/Cs\H3/Cs\H3",
    group = 
"""
1     Cs u0 {2,S} {4,S} {5,S} {6,S}
2  *3 C  u1 {1,S} {3,S} {7,S}
3     Cs u0 {2,S} {8,S} {9,S} {10,S}
4     H  u0 {1,S}
5     H  u0 {1,S}
6     H  u0 {1,S}
7     H  u0 {2,S}
8     H  u0 {3,S}
9     H  u0 {3,S}
10    H  u0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.01865, 'd13': 0.035001, 'd23': 0.050719},
        uncertainties = {'d12': 0.042934, 'd13': 0.032697, 'd23': 0.056341},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 42 distances.
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
""",
)

entry(
    index = 284,
    label = "C_rad/H/NonDeC_5ring_alpha6ring",
    group = 
"""
1  *3 C  u1 {2,S} {3,S} {4,S}
2     H  u0 {1,S}
3     Cs u0 {1,S} {5,S} {7,S}
4     Cs u0 {1,S} {6,S}
5     Cs u0 {3,S} {6,S} {10,S}
6     Cs u0 {4,S} {5,S}
7     C  u0 {3,S} {8,S}
8     C  u0 {7,S} {9,S}
9     C  u0 {8,S} {10,S}
10    C  u0 {5,S} {9,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 285,
    label = "C_rad/H/NonDeC_5ring_beta6ring",
    group = 
"""
1  *3 C  u1 {2,S} {3,S} {4,S}
2     H  u0 {1,S}
3     Cs u0 {1,S} {5,S}
4     Cs u0 {1,S} {6,S}
5     Cs u0 {3,S} {6,S} {7,S}
6     Cs u0 {4,S} {5,S} {10,S}
7     C  u0 {5,S} {8,S}
8     C  u0 {7,S} {9,S}
9     C  u0 {8,S} {10,S}
10    C  u0 {6,S} {9,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 286,
    label = "C_rad/H/Cs\H2\Cs/Cs\H2\O",
    group = 
"""
1     C  u0 {2,S} {6,S} {7,S} {8,S}
2     Cs u0 {1,S} {3,S} {9,S} {10,S}
3  *3 C  u1 {2,S} {4,S} {11,S}
4     Cs u0 {3,S} {5,S} {12,S} {13,S}
5     O  u0 {4,S} {14,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {1,S}
9     H  u0 {2,S}
10    H  u0 {2,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    H  u0 {4,S}
14    H  u0 {5,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 287,
    label = "C_rad/H/Cs\H\Cs\O/Cs",
    group = 
"""
1     Cs u0 {3,S} {6,S} {7,S} {8,S}
2     Cs u0 {4,S} {9,S} {10,S} {11,S}
3  *3 C  u1 {1,S} {4,S} {12,S}
4     Cs u0 {2,S} {3,S} {5,S} {13,S}
5     Os u0 {4,S} {14,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {1,S}
9     H  u0 {2,S}
10    H  u0 {2,S}
11    H  u0 {2,S}
12    H  u0 {3,S}
13    H  u0 {4,S}
14    H  u0 {5,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 288,
    label = "C_rad/H/Cs\H2\Cs|O/Cs",
    group = 
"""
1     Cs u0 {2,S} {6,S} {7,S} {8,S}
2  *3 C  u1 {1,S} {3,S} {9,S}
3     Cs u0 {2,S} {4,S} {10,S} {11,S}
4     C  u0 {3,S} {5,S} {12,S} {13,S}
5     O  u0 {4,S} {14,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {1,S}
9     H  u0 {2,S}
10    H  u0 {3,S}
11    H  u0 {3,S}
12    H  u0 {4,S}
13    H  u0 {4,S}
14    H  u0 {5,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 289,
    label = "C_rad/H/NonDeO",
    group = 
"""
1 *3 C      u1 {2,S} {3,S} {4,S}
2    H      u0 {1,S}
3    O      u0 {1,S}
4    [Cs,O] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.013797, 'd13': 0.029806, 'd23': 0.023799},
        uncertainties = {'d12': 0.076971, 'd13': 0.044918, 'd23': 0.061106},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 43 distances.
[<Entry index=10 label="O/H/NonDeO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=61 label="C_methane">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=61 label="C_methane">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=72 label="C/H3/O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=11 label="H2O2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=290 label="C_rad/H/CsO">]
""",
)

entry(
    index = 290,
    label = "C_rad/H/CsO",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs u0 {1,S}
4    O  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.015146, 'd13': 0.030165, 'd23': 0.023154},
        uncertainties = {'d12': 0.07674, 'd13': 0.045606, 'd23': 0.061199},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 41 distances.
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=61 label="C_methane">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=72 label="C/H3/O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=11 label="H2O2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=290 label="C_rad/H/CsO">]
""",
)

entry(
    index = 291,
    label = "C_rad/H/Cs\H2\Cs/O",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs u0 {1,S} {5,S} {6,S} {7,S}
4    O  u0 {1,S}
5    H  u0 {3,S}
6    H  u0 {3,S}
7    Cs u0 {3,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 292,
    label = "C_rad/H/Cs\H2\Cs|H2|Cs/O",
    group = 
"""
1     C  u0 {2,S} {6,S} {7,S} {8,S}
2     Cs u0 {1,S} {3,S} {9,S} {10,S}
3     Cs u0 {2,S} {4,S} {11,S} {12,S}
4  *3 C  u1 {3,S} {5,S} {13,S}
5     O  u0 {4,S} {14,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {1,S}
9     H  u0 {2,S}
10    H  u0 {2,S}
11    H  u0 {3,S}
12    H  u0 {3,S}
13    H  u0 {4,S}
14    H  u0 {5,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 293,
    label = "C_rad/H/Cs\H\Cs2/O",
    group = 
"""
1    C  u0 {2,S}
2    Cs u0 {1,S} {3,S} {5,S} {6,S}
3 *3 C  u1 {2,S} {4,S} {7,S}
4    O  u0 {3,S} {8,S}
5    C  u0 {2,S}
6    H  u0 {2,S}
7    H  u0 {3,S}
8    H  u0 {4,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 294,
    label = "C_rad/H/O2",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    O u0 {1,S}
4    O u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.017891, 'd13': 0.021368, 'd23': 0.038954},
        uncertainties = {'d12': 0.744013, 'd13': 0.266247, 'd23': 0.54375},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=61 label="C_methane">, <Entry index=294 label="C_rad/H/O2">]
""",
)

entry(
    index = 295,
    label = "C_rad/H/NonDeS",
    group = 
"""
1 *3 C      u1 {2,S} {3,S} {4,S}
2    H      u0 {1,S}
3    S      u0 {1,S}
4    [Cs,S] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 296,
    label = "C_rad/H/CsS",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    S  u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 297,
    label = "C_rad/H/S2",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    S u0 {1,S}
4    S u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 430,
    label = "C_rad/H/NonDeCN",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    C u0 {1,S}
4    N u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 431,
    label = "C_rad/H/NonDeON",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    O u0 {1,S}
4    N u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 432,
    label = "C_rad/H/NonDeNN",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    N u0 {1,S}
4    N u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 298,
    label = "C_rad/H/OneDe",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S,N]       u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.073748, 'd13': 0.050157, 'd23': -0.024335},
        uncertainties = {'d12': 0.077366, 'd13': 0.055202, 'd23': 0.056998},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 143 distances.
[<Entry index=75 label="C/H3/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=61 label="C_methane">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=4 label="H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=306 label="C_rad/H/OneDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=40 label="Cb_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=61 label="C_methane">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=302 label="C_rad/H/CO/Cs">]
""",
)

entry(
    index = 299,
    label = "C_rad/H/OneDeC",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2    H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    Cs            u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.073382, 'd13': 0.050007, 'd23': -0.024131},
        uncertainties = {'d12': 0.077492, 'd13': 0.05537, 'd23': 0.057104},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 142 distances.
[<Entry index=75 label="C/H3/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=61 label="C_methane">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=4 label="H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=40 label="Cb_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=61 label="C_methane">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=302 label="C_rad/H/CO/Cs">]
""",
)

entry(
    index = 300,
    label = "C_rad/H/CtCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 301,
    label = "C_rad/H/CbCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 302,
    label = "C_rad/H/CO/Cs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs u0 {1,S}
4    CO u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.028622, 'd13': 0.036324, 'd23': 0.00976},
        uncertainties = {'d12': 0.052328, 'd13': 0.031675, 'd23': 0.059825},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 25 distances.
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
""",
)

entry(
    index = 303,
    label = "C_rad/H/CO\H/Cs\H3",
    group = 
"""
1    Cs u0 {2,S} {5,S} {6,S} {7,S}
2 *3 C  u1 {1,S} {3,S} {8,S}
3    CO u0 {2,S} {4,D} {9,S}
4    O  u0 {3,D}
5    H  u0 {1,S}
6    H  u0 {1,S}
7    H  u0 {1,S}
8    H  u0 {2,S}
9    H  u0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.093064, 'd13': 0.052074, 'd23': -0.042865},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
""",
)

entry(
    index = 304,
    label = "C_rad/H/CdCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd u0 {1,S} {5,D}
4    Cs u0 {1,S}
5    C  u0 {3,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.083232, 'd13': 0.053018, 'd23': -0.031589},
        uncertainties = {'d12': 0.082491, 'd13': 0.059577, 'd23': 0.057415},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 117 distances.
[<Entry index=75 label="C/H3/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=40 label="Cb_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=61 label="C_methane">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=304 label="C_rad/H/CdCs">]
""",
)

entry(
    index = 305,
    label = "C_rad/H/CSCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd u0 {1,S} {5,D}
4    Cs u0 {1,S}
5    S  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 306,
    label = "C_rad/H/OneDeO",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2    H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    O             u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.123483, 'd13': 0.07053, 'd23': -0.052021},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=306 label="C_rad/H/OneDeO">]
""",
)

entry(
    index = 307,
    label = "C_rad/H/OneDeS",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    S                u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 308,
    label = "C_rad/H/CtS",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
4    S  u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 309,
    label = "C_rad/H/CbS",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cb u0 {1,S}
4    S  u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 310,
    label = "C_rad/H/CdS",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd u0 {1,S} {5,D}
4    S  u0 {1,S}
5    C  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 311,
    label = "C_rad/H/CSS",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    CS u0 {1,S} {5,D}
4    S  u0 {1,S}
5    S  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 433,
    label = "C_rad/H/OneDeN",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd u0 {1,S}
4    N  u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 312,
    label = "C_rad/H/TwoDe",
    group = 
"""
1 *3 C                u1 {2,S} {3,S} {4,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.12053, 'd13': 0.071121, 'd23': -0.050272},
        uncertainties = {'d12': 0.094092, 'd13': 0.082112, 'd23': 0.05231},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 85 distances.
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=42 label="CO_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=61 label="C_methane">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=40 label="Cb_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
""",
)

entry(
    index = 313,
    label = "C_rad/H/CtCt",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 314,
    label = "C_rad/H/CtCb",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 315,
    label = "C_rad/H/CtCO",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
4    CO u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 316,
    label = "C_rad/H/CbCb",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 317,
    label = "C_rad/H/CbCO",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cb u0 {1,S}
4    CO u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 318,
    label = "C_rad/H/COCO",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    CO u0 {1,S}
4    CO u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 319,
    label = "C_rad/H/CdCt",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd u0 {1,S} {5,D}
4    Ct u0 {1,S}
5    C  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 320,
    label = "C_rad/H/CtCS",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
4    CS u0 {1,S} {5,D}
5    S  u0 {4,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 321,
    label = "C_rad/H/CdCb",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd u0 {1,S} {5,D}
4    Cb u0 {1,S}
5    C  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 322,
    label = "C_rad/H/CbCS",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cb u0 {1,S}
4    CS u0 {1,S} {5,D}
5    S  u0 {4,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 323,
    label = "C_rad/H/CdCO",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd u0 {1,S} {5,D}
4    CO u0 {1,S}
5    C  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 324,
    label = "C_rad/H/COCS",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    CO u0 {1,S}
4    Cd u0 {1,S} {5,D}
5    S  u0 {4,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 325,
    label = "C_rad/H/CdCd",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd u0 {1,S} {5,D}
4    Cd u0 {1,S} {6,D}
5    C  u0 {3,D}
6    C  u0 {4,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.12053, 'd13': 0.071121, 'd23': -0.050272},
        uncertainties = {'d12': 0.094092, 'd13': 0.082112, 'd23': 0.05231},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 85 distances.
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=42 label="CO_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=61 label="C_methane">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=40 label="Cb_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
""",
)

entry(
    index = 326,
    label = "C_rad/H/CdCS",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd u0 {1,S} {5,D}
4    CS u0 {1,S} {6,D}
5    C  u0 {3,D}
6    S  u0 {4,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 327,
    label = "C_rad/H/CSCS",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    CS u0 {1,S} {5,D}
4    CS u0 {1,S} {6,D}
5    S  u0 {3,D}
6    S  u0 {4,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 328,
    label = "C_ter_rad",
    group = 
"""
1 *3 C   u1 {2,S} {3,S} {4,S}
2    R!H u0 {1,S}
3    R!H u0 {1,S}
4    R!H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.062953, 'd13': 0.047071, 'd23': -0.014477},
        uncertainties = {'d12': 0.072212, 'd13': 0.073142, 'd23': 0.046},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 91 distances.
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=4 label="H2">, <Entry index=335 label="C_rad/Cs2O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=11 label="H2O2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=443 label="OH_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=61 label="C_methane">, <Entry index=374 label="C_rad/CdCdCs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=61 label="C_methane">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=42 label="CO_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=7 label="O_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
""",
)

entry(
    index = 329,
    label = "C_rad/NonDe",
    group = 
"""
1 *3 C        u1 {2,S} {3,S} {4,S}
2    [Cs,O,S] u0 {1,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.003742, 'd13': 0.014541, 'd23': 0.009073},
        uncertainties = {'d12': 0.133591, 'd13': 0.144725, 'd23': 0.063605},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 16 distances.
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=4 label="H2">, <Entry index=335 label="C_rad/Cs2O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=42 label="CO_pri">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=11 label="H2O2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=72 label="C/H3/O">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=4 label="H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=40 label="Cb_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=330 label="C_rad/Cs3">]
""",
)

entry(
    index = 330,
    label = "C_rad/Cs3",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.0056, 'd13': 0.021566, 'd23': 0.01431},
        uncertainties = {'d12': 0.059071, 'd13': 0.052371, 'd23': 0.064157},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 15 distances.
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=42 label="CO_pri">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=11 label="H2O2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=72 label="C/H3/O">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=4 label="H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=40 label="Cb_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=330 label="C_rad/Cs3">]
""",
)

entry(
    index = 331,
    label = "C_rad/Cs2/Cs\O",
    group = 
"""
1    Cs u0 {2,S}
2 *3 C  u1 {1,S} {3,S} {5,S}
3    Cs u0 {2,S} {4,S}
4    O  u0 {3,S}
5    Cs u0 {2,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 332,
    label = "C_rad/Cs3_5ring_fused6",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cs u0 {1,S} {5,S}
3    Cs u0 {1,S} {6,S}
4    Cs u0 {1,S} {7,S}
5    Cs u0 {2,S} {6,S}
6    Cs u0 {3,S} {5,S} {7,S}
7    Cs u0 {4,S} {6,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 333,
    label = "C_rad/Cs3_5ring_adj5",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cs u0 {1,S} {5,S}
3    Cs u0 {1,S} {6,S} {8,S}
4    Cs u0 {1,S} {7,S}
5    Cs u0 {2,S} {6,S}
6    Cs u0 {3,S} {5,S}
7    Cs u0 {4,S} {8,S}
8    Cs u0 {3,S} {7,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 334,
    label = "C_rad/NDMustO",
    group = 
"""
1 *3 C      u1 {2,S} {3,S} {4,S}
2    O      u0 {1,S}
3    [Cs,O] u0 {1,S}
4    [Cs,O] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.043944, 'd13': -0.16577, 'd23': -0.125363},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=335 label="C_rad/Cs2O">]
""",
)

entry(
    index = 335,
    label = "C_rad/Cs2O",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    O  u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.043944, 'd13': -0.16577, 'd23': -0.125363},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=4 label="H2">, <Entry index=335 label="C_rad/Cs2O">]
""",
)

entry(
    index = 336,
    label = "C_rad/OOH/Cs/Cs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    O  u0 {1,S} {5,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    O  u0 {2,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 337,
    label = "C_rad/O/Cs/Cs\Cs",
    group = 
"""
1     C  u0 {3,S} {6,S} {7,S} {8,S}
2     Cs u0 {4,S} {9,S} {10,S} {11,S}
3     Cs u0 {1,S} {4,S} {12,S} {13,S}
4  *3 C  u1 {2,S} {3,S} {5,S}
5     O  u0 {4,S} {14,S}
6     H  u0 {1,S}
7     H  u0 {1,S}
8     H  u0 {1,S}
9     H  u0 {2,S}
10    H  u0 {2,S}
11    H  u0 {2,S}
12    H  u0 {3,S}
13    H  u0 {3,S}
14    H  u0 {5,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 338,
    label = "C_rad/CsO2",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    O  u0 {1,S}
3    O  u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 339,
    label = "C_rad/O3",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    O u0 {1,S}
3    O u0 {1,S}
4    O u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 340,
    label = "C_rad/NDMustS",
    group = 
"""
1 *3 C      u1 {2,S} {3,S} {4,S}
2    S      u0 {1,S}
3    [Cs,S] u0 {1,S}
4    [Cs,S] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 341,
    label = "C_rad/Cs2S",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    S  u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 342,
    label = "C_rad/CsS2",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    S  u0 {1,S}
3    S  u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 343,
    label = "C_rad/S3",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2    S u0 {1,S}
3    S u0 {1,S}
4    S u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 344,
    label = "C_rad/OneDe",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cs,O,S]      u0 {1,S}
4    [Cs,O,S]      u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.072414, 'd13': 0.052275, 'd23': -0.018087},
        uncertainties = {'d12': 0.055407, 'd13': 0.053493, 'd23': 0.042183},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 74 distances.
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=443 label="OH_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=61 label="C_methane">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=7 label="O_pri">, <Entry index=348 label="C_rad/COCs2">]
""",
)

entry(
    index = 345,
    label = "C_rad/Cs2",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    Cs            u0 {1,S}
4    Cs            u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.072414, 'd13': 0.052275, 'd23': -0.018087},
        uncertainties = {'d12': 0.055407, 'd13': 0.053493, 'd23': 0.042183},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 74 distances.
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=443 label="OH_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=61 label="C_methane">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=7 label="O_pri">, <Entry index=348 label="C_rad/COCs2">]
""",
)

entry(
    index = 346,
    label = "C_rad/CtCs2",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 347,
    label = "C_rad/CbCs2",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 348,
    label = "C_rad/COCs2",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.072414, 'd13': 0.052275, 'd23': -0.018087},
        uncertainties = {'d12': 0.055407, 'd13': 0.053493, 'd23': 0.042183},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 74 distances.
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=443 label="OH_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=61 label="C_methane">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=7 label="O_pri">, <Entry index=348 label="C_rad/COCs2">]
""",
)

entry(
    index = 349,
    label = "C_rad/CdCs2",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 350,
    label = "C_rad/CSCs2",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    S  u0 {2,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 351,
    label = "C_rad/CsO",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    O             u0 {1,S}
4    Cs            u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 352,
    label = "C_rad/CsS",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    S             u0 {1,S}
4    Cs            u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 353,
    label = "C_rad/CtCsS",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    S  u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 354,
    label = "C_rad/CbCsS",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    S  u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 355,
    label = "C_rad/CdCsS",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    S  u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 356,
    label = "C_rad/CSCsS",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    S  u0 {1,S}
4    Cs u0 {1,S}
5    S  u0 {2,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 357,
    label = "C_rad/O2",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    O             u0 {1,S}
4    O             u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 358,
    label = "C_rad/OS",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    S             u0 {1,S}
4    O             u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 359,
    label = "C_rad/S2",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    S             u0 {1,S}
4    S             u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 360,
    label = "C_rad/TwoDe",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cs,O,S]      u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.270274, 'd13': 0.160326, 'd23': -0.112731},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=61 label="C_methane">, <Entry index=374 label="C_rad/CdCdCs">]
""",
)

entry(
    index = 361,
    label = "C_rad/Cs",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    Cs            u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.270274, 'd13': 0.160326, 'd23': -0.112731},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=61 label="C_methane">, <Entry index=374 label="C_rad/CdCdCs">]
""",
)

entry(
    index = 362,
    label = "C_rad/CtCtCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 363,
    label = "C_rad/CtCbCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 364,
    label = "C_rad/CtCOCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 365,
    label = "C_rad/CbCbCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 366,
    label = "C_rad/CbCOCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 367,
    label = "C_rad/COCOCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 368,
    label = "C_rad/CdCtCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 369,
    label = "C_rad/CtCSCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cd u0 {1,S} {5,D}
4    Cs u0 {1,S}
5    S  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 370,
    label = "C_rad/CdCbCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 371,
    label = "C_rad/CbCSCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cd u0 {1,S} {5,D}
4    Cs u0 {1,S}
5    S  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 372,
    label = "C_rad/CdCOCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CO u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 373,
    label = "C_rad/COCSCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    Cd u0 {1,S} {5,D}
4    Cs u0 {1,S}
5    S  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 374,
    label = "C_rad/CdCdCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cd u0 {1,S} {6,D}
4    Cs u0 {1,S}
5    C  u0 {2,D}
6    C  u0 {3,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.270274, 'd13': 0.160326, 'd23': -0.112731},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=61 label="C_methane">, <Entry index=374 label="C_rad/CdCdCs">]
""",
)

entry(
    index = 375,
    label = "C_rad/CdCSCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cd u0 {1,S} {6,D}
4    Cs u0 {1,S}
5    C  u0 {2,D}
6    S  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 376,
    label = "C_rad/CSCSCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cd u0 {1,S} {6,D}
4    Cs u0 {1,S}
5    S  u0 {2,D}
6    S  u0 {3,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 377,
    label = "C_rad/TDMustO",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    O             u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 378,
    label = "C_rad/TDMustS",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    S             u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 379,
    label = "C_rad/ThreeDe",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 434,
    label = "N3_rad",
    group = 
"""
1 *3 [N3s,N3d] u1
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 435,
    label = "N3s_rad",
    group = 
"""
1 *3 N3s u1
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 436,
    label = "NH2_rad",
    group = 
"""
1 *3 N3s u1 {2,S} {3,S}
2    H   u0 {1,S}
3    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 437,
    label = "N3s_rad_pri",
    group = 
"""
1 *3 N3s u1 {2,S} {3,S}
2    H   u0 {1,S}
3    R!H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 438,
    label = "N3s_rad_sec",
    group = 
"""
1 *3 N3s u1 {2,S} {3,S}
2    R!H u0 {1,S}
3    R!H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 439,
    label = "N3d_rad",
    group = 
"""
1 *3 N3d u1 {2,D}
2    R!H u0 {1,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 462,
    label = "N3d_rad/OneDe",
    group = 
"""
1 *3 N3d      u1 {2,D}
2    [Cd,Cdd] u0 {1,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 463,
    label = "N3d_rad/OneDeC",
    group = 
"""
1 *3 N3d u1 {2,D}
2    Cdd u0 {1,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 464,
    label = "N3d_rad/OneDeCdd_O",
    group = 
"""
1 *3 N3d u1 {2,D}
2    Cdd u0 {1,D} {3,D}
3    Od  u0 {2,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 440,
    label = "N5_rad",
    group = 
"""
1 *3 [N5s,N5d,N5t] u1
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 441,
    label = "N5d_rad",
    group = 
"""
1 *3 N5d u1
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: X_H_or_Xrad_H_Xbirad_H_Xtrirad_H
    L2: X_H
        L3: H2
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
                    L6: S/H/Ct
                    L6: S/H/Cb
                    L6: S/H/CO
                    L6: S/H/Cd
                    L6: S/H/CS
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
                    L6: Cd/H/Ct
                    L6: Cd/H/Cb
                    L6: Cd/H/CO
                    L6: Cd/H/Cd
                    L6: Cd/H/CS
                    L6: Cd/H/DeN
        L3: Cb_H
        L3: CO_H
            L4: CO_pri
            L4: CO_sec
                L5: CO/H/NonDe
                    L6: CO/H/Cs
                        L7: CO/H/Cs\Cs|Cs
                L5: CO/H/OneDe
        L3: CS_H
            L4: CS_pri
            L4: CS_sec
                L5: CS/H/NonDeC
                L5: CS/H/NonDeO
                L5: CS/H/NonDeS
                L5: CS/H/OneDe
                    L6: CS/H/Ct
                    L6: CS/H/Cb
                    L6: CS/H/CO
                    L6: CS/H/Cd
                    L6: CS/H/CS
        L3: Cs_H
            L4: C_methane
            L4: C_pri
                L5: C/H3/Cs
                    L6: C/H3/Cs\H3
                    L6: C/H3/Cs\OneNonDe
                        L7: C/H3/Cs\H2\Cs
                            L8: C/H3/Cs\H2\Cs|O
                        L7: C/H3/Cs\H2\O
                    L6: C/H3/Cs\TwoNonDe
                        L7: C/H3/Cs\H\Cs\O
                        L7: C/H3/Cs\H\Cs\Cs|O
                L5: C/H3/O
                L5: C/H3/S
                L5: C/H3/OneDe
                    L6: C/H3/Ct
                    L6: C/H3/Cb
                    L6: C/H3/CO
                    L6: C/H3/Cd
                        L7: C/H3/Cd\H_Cd\H2
                        L7: C/H3/Cd\H_Cd\H\Cs
                        L7: C/H3/Cd\Cs_Cd\H2
                    L6: C/H3/CS
                L5: Cs/H3/NonDeN
                L5: Cs/H3/OneDeN
            L4: C_sec
                L5: C/H2/NonDeC
                    L6: C/H2/Cs/Cs\O
                    L6: C/H2/Cs/Cs\Cs|O
                    L6: C/H2/NonDeC_5ring
                        L7: C/H2/NonDeC_5ring_fused6_1
                        L7: C/H2/NonDeC_5ring_fused6_2
                        L7: C/H2/NonDeC_5ring_alpha6ring
                        L7: C/H2/NonDeC_5ring_beta6ring
                    L6: C/H2/Cs\H3/Cs\H3
                L5: C/H2/NonDeO
                    L6: C/H2/CsO
                        L7: C/H2/Cs\Cs2/O
                    L6: C/H2/O2
                L5: C/H2/NonDeS
                    L6: C/H2/CsS
                L5: C/H2/NonDeN
                L5: C/H2/OneDe
                    L6: C/H2/OneDeC
                        L7: C/H2/CtCs
                        L7: C/H2/CbCs
                        L7: C/H2/COCs
                            L8: C/H2/CO\H/Cs\H3
                        L7: C/H2/CdCs
                            L8: C/H2/Cd\H_Cd\H2/Cs\H3
                        L7: C/H2/CSCs
                    L6: C/H2/OneDeO
                    L6: C/H2/OneDeS
                        L7: C/H2/CbS
                        L7: C/H2/CtS
                        L7: C/H2/CdS
                        L7: C/H2/CSS
                L5: C/H2/TwoDe
                    L6: C/H2/CtCt
                    L6: C/H2/CtCb
                    L6: C/H2/CtCO
                    L6: C/H2/CbCb
                    L6: C/H2/CbCO
                    L6: C/H2/COCO
                    L6: C/H2/CdCt
                    L6: C/H2/CtCS
                    L6: C/H2/CdCb
                    L6: C/H2/CbCS
                    L6: C/H2/CdCO
                    L6: C/H2/COCS
                    L6: C/H2/CdCd
                    L6: C/H2/CdCS
                    L6: C/H2/CSCS
                L5: C/H2/Cb
            L4: C_ter
                L5: C/H/NonDe
                    L6: C/H/Cs3
                        L7: C/H/Cs3_5ring
                            L8: C/H/Cs3_5ring_fused6
                            L8: C/H/Cs3_5ring_adj5
                        L7: C/H/Cs2/Cs\O
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
                        L7: C/H/Cs2Ct
                        L7: C/H/Cs2Cb
                        L7: C/H/Cs2CO
                        L7: C/H/Cs2Cd
                        L7: C/H/Cs2CS
                    L6: C/H/CsO
                    L6: C/H/CsS
                        L7: C/H/CbCsS
                        L7: C/H/CtCsS
                        L7: C/H/CdCsS
                        L7: C/H/CSCsS
                    L6: C/H/OO
                    L6: C/H/OS
                    L6: C/H/SS
                L5: C/H/TwoDe
                    L6: C/H/Cs
                        L7: C/H/CtCt
                        L7: C/H/CtCb
                        L7: C/H/CtCO
                        L7: C/H/CbCb
                        L7: C/H/CbCO
                        L7: C/H/COCO
                        L7: C/H/CdCt
                        L7: C/H/CtCS
                        L7: C/H/CdCb
                        L7: C/H/CbCS
                        L7: C/H/CdCO
                        L7: C/H/COCS
                        L7: C/H/CdCd
                        L7: C/H/CdCS
                        L7: C/H/CSCS
                    L6: C/H/TDMustO
                    L6: C/H/TDMustS
                L5: C/H/ThreeDe
                L5: C/H/Cb
        L3: N3_H
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
            L4: N3d_H
                L5: N3d/H/NonDe
                    L6: N3d/H/NonDeC
                    L6: N3d/H/NonDeO
                    L6: N3d/H/NonDeN
                L5: N3d/H/OneDe
                    L6: N3d/H/OneDeCO
                    L6: N3d/H/OneDeN
        L3: N5_H
            L4: N5d_H
                L5: N5d/H/NonDeOO
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
        L3: CH2_triplet_H
        L3: CH2_singlet_H
        L3: NH_triplet_H
        L3: NH_singlet_H
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
        L3: CH2_triplet
        L3: CH2_singlet
        L3: NH_triplet
        L3: NH_singlet
    L2: Y_rad
        L3: H_rad
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
                    L6: O_rad/Cs\H2\Cs|H|Cs2
                L5: O_rad/NonDeO
                    L6: OOC
                L5: O_rad/NonDeN
                L5: O_rad/OneDe
                    L6: O_rad/OneDeC
                        L7: O_rad/Cd
                            L8: O_rad/Cd\H_Cd\H2
                            L8: O_rad/Cd\H_Cd\H\Cs
                            L8: O_rad/Cd\H_Cd\Cs2
                            L8: O_rad/Cd\Cs_Cd\H2
                            L8: O_rad/Cd\Cs_Cd\H\Cs
                            L8: O_rad/Cd\Cs_Cd\Cs2
                    L6: InChI=1S/NO3/c2-1(3)4
                    L6: O_rad/OneDeN
        L3: S_rad
            L4: S_pri_rad
            L4: S_sec_rad
                L5: S_rad/NonDeC
                L5: S_rad/NonDeS
                L5: S_rad/OneDe
                    L6: S_rad/Ct
                    L6: S_rad/Cb
                    L6: S_rad/CO
                    L6: S_rad/Cd
                    L6: S_rad/CS
        L3: Cd_rad
            L4: Cd_pri_rad
                L5: Cd_Cd\H2_pri_rad
                L5: Cd_Cd\H\Cs_pri_rad
                    L6: Cd_Cd\H\Cs|H2|Cs_pri_rad
                L5: Cd_Cd\Cs2_pri_rad
            L4: Cd_sec_rad
                L5: Cd_rad/NonDeC
                    L6: Cd_Cd\H2_rad/Cs
                    L6: Cd_Cd\H\Cs_rad/Cs
                L5: Cd_rad/NonDeO
                L5: Cd_rad/NonDeS
                L5: Cd_rad/NonDeN
                L5: Cd_rad/OneDe
                    L6: Cd_rad/Ct
                    L6: Cd_rad/Cb
                    L6: Cd_rad/CO
                    L6: Cd_rad/Cd
                    L6: Cd_rad/CS
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
                    L6: CS_rad/Ct
                    L6: CS_rad/Cb
                    L6: CS_rad/CO
                    L6: CS_rad/Cd
                    L6: CS_rad/CS
        L3: Cs_rad
            L4: C_methyl
            L4: C_pri_rad
                L5: C_rad/H2/Cs
                    L6: C_rad/H2/Cs\H3
                    L6: C_rad/H2/Cs\Cs2\O
                    L6: C_rad/H2/Cs\H\Cs\Cs|O
                    L6: C_rad/H2/Cs\H\Cs|Cs\O
                    L6: C_rad/H2/Cs\H2\Cs|Cs|O
                    L6: C_rad/H2/Cs\H2\Cs|Cs#O
                L5: C_rad/H2/Ct
                L5: C_rad/H2/Cb
                L5: C_rad/H2/CO
                L5: C_rad/H2/O
                L5: C_rad/H2/S
                L5: C_rad/H2/Cd
                    L6: C_rad/H2/Cd\H_Cd\H2
                    L6: C_rad/H2/Cd\Cs_Cd\H2
                L5: C_rad/H2/CS
                L5: C_rad/H2/N
            L4: C_sec_rad
                L5: C_rad/H/NonDeC
                    L6: C_rad/H/NonDeC_5ring_fused6_1
                    L6: C_rad/H/NonDeC_5ring_fused6_2
                    L6: C_rad/H/Cs\H3/Cs\H3
                    L6: C_rad/H/NonDeC_5ring_alpha6ring
                    L6: C_rad/H/NonDeC_5ring_beta6ring
                    L6: C_rad/H/Cs\H2\Cs/Cs\H2\O
                    L6: C_rad/H/Cs\H\Cs\O/Cs
                    L6: C_rad/H/Cs\H2\Cs|O/Cs
                L5: C_rad/H/NonDeO
                    L6: C_rad/H/CsO
                        L7: C_rad/H/Cs\H2\Cs/O
                            L8: C_rad/H/Cs\H2\Cs|H2|Cs/O
                        L7: C_rad/H/Cs\H\Cs2/O
                    L6: C_rad/H/O2
                L5: C_rad/H/NonDeS
                    L6: C_rad/H/CsS
                    L6: C_rad/H/S2
                L5: C_rad/H/NonDeCN
                L5: C_rad/H/NonDeON
                L5: C_rad/H/NonDeNN
                L5: C_rad/H/OneDe
                    L6: C_rad/H/OneDeC
                        L7: C_rad/H/CtCs
                        L7: C_rad/H/CbCs
                        L7: C_rad/H/CO/Cs
                            L8: C_rad/H/CO\H/Cs\H3
                        L7: C_rad/H/CdCs
                        L7: C_rad/H/CSCs
                    L6: C_rad/H/OneDeO
                    L6: C_rad/H/OneDeS
                        L7: C_rad/H/CtS
                        L7: C_rad/H/CbS
                        L7: C_rad/H/CdS
                        L7: C_rad/H/CSS
                    L6: C_rad/H/OneDeN
                L5: C_rad/H/TwoDe
                    L6: C_rad/H/CtCt
                    L6: C_rad/H/CtCb
                    L6: C_rad/H/CtCO
                    L6: C_rad/H/CbCb
                    L6: C_rad/H/CbCO
                    L6: C_rad/H/COCO
                    L6: C_rad/H/CdCt
                    L6: C_rad/H/CtCS
                    L6: C_rad/H/CdCb
                    L6: C_rad/H/CbCS
                    L6: C_rad/H/CdCO
                    L6: C_rad/H/COCS
                    L6: C_rad/H/CdCd
                    L6: C_rad/H/CdCS
                    L6: C_rad/H/CSCS
            L4: C_ter_rad
                L5: C_rad/NonDe
                    L6: C_rad/Cs3
                        L7: C_rad/Cs2/Cs\O
                        L7: C_rad/Cs3_5ring_fused6
                        L7: C_rad/Cs3_5ring_adj5
                    L6: C_rad/NDMustO
                        L7: C_rad/Cs2O
                            L8: C_rad/OOH/Cs/Cs
                            L8: C_rad/O/Cs/Cs\Cs
                        L7: C_rad/CsO2
                        L7: C_rad/O3
                    L6: C_rad/NDMustS
                        L7: C_rad/Cs2S
                        L7: C_rad/CsS2
                        L7: C_rad/S3
                L5: C_rad/OneDe
                    L6: C_rad/Cs2
                        L7: C_rad/CtCs2
                        L7: C_rad/CbCs2
                        L7: C_rad/COCs2
                        L7: C_rad/CdCs2
                        L7: C_rad/CSCs2
                    L6: C_rad/CsO
                    L6: C_rad/CsS
                        L7: C_rad/CtCsS
                        L7: C_rad/CbCsS
                        L7: C_rad/CdCsS
                        L7: C_rad/CSCsS
                    L6: C_rad/O2
                    L6: C_rad/OS
                    L6: C_rad/S2
                L5: C_rad/TwoDe
                    L6: C_rad/Cs
                        L7: C_rad/CtCtCs
                        L7: C_rad/CtCbCs
                        L7: C_rad/CtCOCs
                        L7: C_rad/CbCbCs
                        L7: C_rad/CbCOCs
                        L7: C_rad/COCOCs
                        L7: C_rad/CdCtCs
                        L7: C_rad/CtCSCs
                        L7: C_rad/CdCbCs
                        L7: C_rad/CbCSCs
                        L7: C_rad/CdCOCs
                        L7: C_rad/COCSCs
                        L7: C_rad/CdCdCs
                        L7: C_rad/CdCSCs
                        L7: C_rad/CSCSCs
                    L6: C_rad/TDMustO
                    L6: C_rad/TDMustS
                L5: C_rad/ThreeDe
        L3: N3_rad
            L4: N3s_rad
                L5: NH2_rad
                L5: N3s_rad_pri
                L5: N3s_rad_sec
            L4: N3d_rad
                L5: N3d_rad/OneDe
                    L6: N3d_rad/OneDeC
                        L7: N3d_rad/OneDeCdd_O
        L3: N5_rad
            L4: N5d_rad
"""
)

