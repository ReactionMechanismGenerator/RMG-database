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
        distances = {'d12': 1.33601, 'd13': 2.66756, 'd23': 1.33633},
        uncertainties = {'d12': 0.07996, 'd13': 0.06712, 'd23': 0.078989},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2142 distances.
[<Entry index=38 label="Cd/H/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=7 label="O_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=11 label="H2O2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=61 label="C_methane">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=4 label="H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=72 label="C/H3/O">, <Entry index=261 label="C_methyl">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
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
[<Entry index=443 label="OH_rad_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=192 label="H_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=42 label="CO_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=4 label="H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=261 label="C_methyl">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=61 label="C_methane">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=13 label="ROOH_sec">, <Entry index=194 label="O2b">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=241 label="Cb_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=194 label="O2b">]
[<Entry index=61 label="C_methane">, <Entry index=374 label="C_rad/CdCdCs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=16 label="Orad_O_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=40 label="Cb_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=241 label="Cb_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=96 label="C/H2/O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=42 label="CO_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=232 label="Cd_Cd\H\Cs_rad/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=272 label="C_rad/H2/CO">]
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
[<Entry index=38 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=192 label="H_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=4 label="H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=4 label="H2">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=261 label="C_methyl">]
[<Entry index=72 label="C/H3/O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=42 label="CO_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=192 label="H_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=194 label="O2b">]
[<Entry index=61 label="C_methane">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=192 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=61 label="C_methane">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=4 label="H2">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=273 label="C_rad/H2/O">]
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
[<Entry index=127 label="C/H2/CdCd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=7 label="O_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=198 label="O_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=443 label="OH_rad_H">, <Entry index=261 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=203 label="OOC">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=194 label="O2b">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=16 label="Orad_O_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=4 label="H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=443 label="OH_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=194 label="O2b">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/O">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=245 label="CO_rad/NonDe">]
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
[<Entry index=94 label="C/H2/CsO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=108 label="C/H2/OneDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=194 label="O2b">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
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
[<Entry index=35 label="Cd/H/Ct">, <Entry index=243 label="CO_pri_rad">]
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
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=241 label="Cb_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=67 label="C/H3/Cs\H2\Cs|O">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=192 label="H_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=42 label="CO_pri">, <Entry index=192 label="H_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=241 label="Cb_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=42 label="CO_pri">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=61 label="C_methane">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=61 label="C_methane">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=4 label="H2">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=61 label="C_methane">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=198 label="O_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=241 label="Cb_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=72 label="C/H3/O">, <Entry index=203 label="OOC">]
[<Entry index=40 label="Cb_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=139 label="C/H/Cs2O">, <Entry index=192 label="H_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=241 label="Cb_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=192 label="H_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H2/Cs\H2\Cs|Cs#O">]
[<Entry index=42 label="CO_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=178 label="C/H/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=306 label="C_rad/H/OneDeO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=61 label="C_methane">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=241 label="Cb_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=261 label="C_methyl">]
[<Entry index=42 label="CO_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=11 label="H2O2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=4 label="H2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=192 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=192 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=236 label="Cd_rad/Ct">]
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
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=241 label="Cb_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=72 label="C/H3/O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=42 label="CO_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=273 label="C_rad/H2/O">]
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
[<Entry index=35 label="Cd/H/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=335 label="C_rad/Cs2O">]
[<Entry index=7 label="O_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
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
[<Entry index=105 label="C/H2/CdCs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=14 label="ROOH_ter">, <Entry index=261 label="C_methyl">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=241 label="Cb_rad">]
[<Entry index=61 label="C_methane">, <Entry index=203 label="OOC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=203 label="OOC">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=241 label="Cb_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=40 label="Cb_H">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=241 label="Cb_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=40 label="Cb_H">, <Entry index=198 label="O_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=16 label="Orad_O_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
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
[<Entry index=40 label="Cb_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=11 label="H2O2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=203 label="OOC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=203 label="OOC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=192 label="H_rad">]
[<Entry index=61 label="C_methane">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=194 label="O2b">]
[<Entry index=443 label="OH_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=192 label="H_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
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
[<Entry index=47 label="CO/H/OneDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=454 label="O/H/OneDeC">, <Entry index=192 label="H_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=61 label="C_methane">, <Entry index=198 label="O_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=198 label="O_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=96 label="C/H2/O2">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=491 label="O_rad/OneDeC">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=203 label="OOC">]
[<Entry index=42 label="CO_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=192 label="H_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=203 label="OOC">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=203 label="OOC">]
[<Entry index=16 label="Orad_O_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=194 label="O2b">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=7 label="O_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=239 label="Cd_rad/Cd">]
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
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=40 label="Cb_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=61 label="C_methane">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
""",
)

entry(
    index = 2,
    label = "Y_rad_birad_trirad_quadrad",
    group = "OR{Y_2centeradjbirad, Y_1centerbirad, Y_rad, Y_1centertrirad, Y_1centerquadrad}",
    distances = DistanceData(distances={}),
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
        distances = {'d12': -0.002556, 'd13': 0.000227, 'd23': 0.002864},
        uncertainties = {'d12': 0.079582, 'd13': 0.066889, 'd23': 0.079185},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2089 distances.
[<Entry index=38 label="Cd/H/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=7 label="O_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=11 label="H2O2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=61 label="C_methane">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=4 label="H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=72 label="C/H3/O">, <Entry index=261 label="C_methyl">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
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
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=42 label="CO_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=4 label="H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=261 label="C_methyl">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=61 label="C_methane">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=13 label="ROOH_sec">, <Entry index=194 label="O2b">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=241 label="Cb_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=194 label="O2b">]
[<Entry index=61 label="C_methane">, <Entry index=374 label="C_rad/CdCdCs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=16 label="Orad_O_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=40 label="Cb_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=241 label="Cb_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=96 label="C/H2/O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=42 label="CO_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=232 label="Cd_Cd\H\Cs_rad/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=42 label="CO_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=272 label="C_rad/H2/CO">]
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
[<Entry index=38 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=192 label="H_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=4 label="H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=4 label="H2">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=261 label="C_methyl">]
[<Entry index=72 label="C/H3/O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=42 label="CO_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=192 label="H_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=192 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=61 label="C_methane">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=4 label="H2">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=40 label="Cb_H">, <Entry index=243 label="CO_pri_rad">]
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
[<Entry index=127 label="C/H2/CdCd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=7 label="O_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=198 label="O_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=194 label="O2b">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=40 label="Cb_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=16 label="Orad_O_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=4 label="H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=194 label="O2b">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/O">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=245 label="CO_rad/NonDe">]
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
[<Entry index=94 label="C/H2/CsO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=108 label="C/H2/OneDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=194 label="O2b">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
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
[<Entry index=35 label="Cd/H/Ct">, <Entry index=243 label="CO_pri_rad">]
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
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=241 label="Cb_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=67 label="C/H3/Cs\H2\Cs|O">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=192 label="H_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=42 label="CO_pri">, <Entry index=192 label="H_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=241 label="Cb_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=42 label="CO_pri">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=61 label="C_methane">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=61 label="C_methane">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=198 label="O_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=241 label="Cb_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=72 label="C/H3/O">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=139 label="C/H/Cs2O">, <Entry index=192 label="H_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=241 label="Cb_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=192 label="H_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H2/Cs\H2\Cs|Cs#O">]
[<Entry index=42 label="CO_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=178 label="C/H/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=306 label="C_rad/H/OneDeO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=61 label="C_methane">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=241 label="Cb_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=261 label="C_methyl">]
[<Entry index=42 label="CO_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=11 label="H2O2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=4 label="H2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=192 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=236 label="Cd_rad/Ct">]
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
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=241 label="Cb_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=72 label="C/H3/O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=42 label="CO_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=273 label="C_rad/H2/O">]
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
[<Entry index=35 label="Cd/H/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=335 label="C_rad/Cs2O">]
[<Entry index=7 label="O_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
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
[<Entry index=105 label="C/H2/CdCs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=14 label="ROOH_ter">, <Entry index=261 label="C_methyl">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=241 label="Cb_rad">]
[<Entry index=61 label="C_methane">, <Entry index=203 label="OOC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=203 label="OOC">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=241 label="Cb_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=72 label="C/H3/O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=40 label="Cb_H">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=241 label="Cb_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=40 label="Cb_H">, <Entry index=198 label="O_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=16 label="Orad_O_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
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
[<Entry index=38 label="Cd/H/Cd">, <Entry index=194 label="O2b">]
[<Entry index=40 label="Cb_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=11 label="H2O2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=203 label="OOC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=203 label="OOC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=192 label="H_rad">]
[<Entry index=61 label="C_methane">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=194 label="O2b">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=192 label="H_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
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
[<Entry index=47 label="CO/H/OneDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=454 label="O/H/OneDeC">, <Entry index=192 label="H_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=61 label="C_methane">, <Entry index=198 label="O_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=198 label="O_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=96 label="C/H2/O2">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=491 label="O_rad/OneDeC">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=203 label="OOC">]
[<Entry index=42 label="CO_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=192 label="H_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=203 label="OOC">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=203 label="OOC">]
[<Entry index=16 label="Orad_O_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=194 label="O2b">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=7 label="O_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=239 label="Cd_rad/Cd">]
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
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=40 label="Cb_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=61 label="C_methane">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=243 label="CO_pri_rad">]
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
        distances = {'d12': -0.327434, 'd13': -0.369886, 'd23': -0.045046},
        uncertainties = {'d12': 0.180387, 'd13': 0.144081, 'd23': 0.112677},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 70 distances.
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
[<Entry index=4 label="H2">, <Entry index=348 label="C_rad/COCs2">]
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
        distances = {'d12': 0.426157, 'd13': 0.120589, 'd23': -0.214467},
        uncertainties = {'d12': 0.201492, 'd13': 0.208459, 'd23': 0.170089},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 12 distances.
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
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
        distances = {'d12': 0.426157, 'd13': 0.120589, 'd23': -0.214467},
        uncertainties = {'d12': 0.201492, 'd13': 0.208459, 'd23': 0.170089},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 12 distances.
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
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
        distances = {'d12': -0.110714, 'd13': -0.149127, 'd23': -0.034542},
        uncertainties = {'d12': 0.097847, 'd13': 0.075496, 'd23': 0.097064},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 203 distances.
[<Entry index=11 label="H2O2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=194 label="O2b">]
[<Entry index=11 label="H2O2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=12 label="ROOH_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=192 label="H_rad">]
[<Entry index=7 label="O_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=11 label="H2O2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=11 label="H2O2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=194 label="O2b">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=192 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=203 label="OOC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="Cb_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=454 label="O/H/OneDeC">, <Entry index=192 label="H_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=304 label="C_rad/H/CdCs">]
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
[<Entry index=11 label="H2O2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=7 label="O_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=11 label="H2O2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=7 label="O_pri">, <Entry index=192 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=203 label="OOC">]
[<Entry index=7 label="O_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=261 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=14 label="ROOH_ter">, <Entry index=261 label="C_methyl">]
[<Entry index=7 label="O_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=11 label="H2O2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=348 label="C_rad/COCs2">]
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
        distances = {'d12': 0.075716, 'd13': -0.158817, 'd23': -0.1997},
        uncertainties = {'d12': 0.191477, 'd13': 0.175539, 'd23': 0.061939},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 14 distances.
[<Entry index=7 label="O_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=7 label="O_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=7 label="O_pri">, <Entry index=192 label="H_rad">]
[<Entry index=7 label="O_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
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
        distances = {'d12': -0.122296, 'd13': -0.148525, 'd23': -0.024281},
        uncertainties = {'d12': 0.090456, 'd13': 0.065977, 'd23': 0.099554},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 189 distances.
[<Entry index=11 label="H2O2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=261 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=194 label="O2b">]
[<Entry index=11 label="H2O2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=12 label="ROOH_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=192 label="H_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=11 label="H2O2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=11 label="H2O2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=194 label="O2b">]
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
[<Entry index=11 label="H2O2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=454 label="O/H/OneDeC">, <Entry index=192 label="H_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=304 label="C_rad/H/CdCs">]
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
[<Entry index=11 label="H2O2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=11 label="H2O2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=261 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=14 label="ROOH_ter">, <Entry index=261 label="C_methyl">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=11 label="H2O2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=348 label="C_rad/COCs2">]
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
        distances = {'d12': -0.06177, 'd13': -0.156862, 'd23': -0.091698},
        uncertainties = {'d12': 0.068277, 'd13': 0.068731, 'd23': 0.051452},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 51 distances.
[<Entry index=9 label="O/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
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
[<Entry index=9 label="O/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
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
        distances = {'d12': -0.143, 'd13': -0.14465, 'd23': -0.000215},
        uncertainties = {'d12': 0.098383, 'd13': 0.050937, 'd23': 0.106965},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 137 distances.
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
[<Entry index=11 label="H2O2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=263 label="C_rad/H2/Cs">]
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
[<Entry index=10 label="O/H/NonDeO">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=194 label="O2b">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=11 label="H2O2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=14 label="ROOH_ter">, <Entry index=261 label="C_methyl">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=203 label="OOC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="Cb_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=192 label="H_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=261 label="C_methyl">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=11 label="H2O2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=11 label="H2O2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=194 label="O2b">]
[<Entry index=11 label="H2O2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=13 label="ROOH_sec">, <Entry index=194 label="O2b">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=236 label="Cd_rad/Ct">]
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
        distances = {'d12': -0.172464, 'd13': -0.143076, 'd23': 0.030481},
        uncertainties = {'d12': 0.067822, 'd13': 0.066715, 'd23': 0.108954},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 37 distances.
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
[<Entry index=11 label="H2O2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="Cb_rad">]
[<Entry index=11 label="H2O2">, <Entry index=192 label="H_rad">]
[<Entry index=11 label="H2O2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=11 label="H2O2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=11 label="H2O2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=304 label="C_rad/H/CdCs">]
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
        distances = {'d12': -0.164228, 'd13': -0.141922, 'd23': 0.023011},
        uncertainties = {'d12': 0.058566, 'd13': 0.046876, 'd23': 0.081238},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 31 distances.
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=203 label="OOC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=194 label="O2b">]
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
        distances = {'d12': -0.023183, 'd13': -0.174787, 'd23': -0.146971},
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
        distances = {'d12': -0.216642, 'd13': -0.117164, 'd23': 0.096657},
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
        distances = {'d12': -0.241135, 'd13': -0.383406, 'd23': -0.13883},
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
        distances = {'d12': -0.241135, 'd13': -0.383406, 'd23': -0.13883},
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
        distances = {'d12': -0.244636, 'd13': -0.064615, 'd23': 0.181811},
        uncertainties = {'d12': 0.084844, 'd13': 0.095037, 'd23': 0.132823},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 22 distances.
[<Entry index=16 label="Orad_O_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=16 label="Orad_O_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=203 label="OOC">]
[<Entry index=16 label="Orad_O_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=16 label="Orad_O_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=239 label="Cd_rad/Cd">]
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
        distances = {'d12': 0.085747, 'd13': 0.017934, 'd23': -0.068103},
        uncertainties = {'d12': 0.119786, 'd13': 0.081365, 'd23': 0.096868},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 319 distances.
[<Entry index=38 label="Cd/H/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=203 label="OOC">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=194 label="O2b">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=246 label="CO_rad/OneDe">]
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
        distances = {'d12': 0.080833, 'd13': 0.015103, 'd23': -0.06576},
        uncertainties = {'d12': 0.131305, 'd13': 0.08275, 'd23': 0.109983},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 210 distances.
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
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
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
        distances = {'d12': 0.080833, 'd13': 0.015103, 'd23': -0.06576},
        uncertainties = {'d12': 0.131305, 'd13': 0.08275, 'd23': 0.109983},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 210 distances.
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
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
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
        distances = {'d12': 0.09534, 'd13': 0.023461, 'd23': -0.07268},
        uncertainties = {'d12': 0.09567, 'd13': 0.079933, 'd23': 0.066171},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 109 distances.
[<Entry index=38 label="Cd/H/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=203 label="OOC">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=194 label="O2b">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=241 label="Cb_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=224 label="Cd_pri_rad">]
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
        distances = {'d12': 0.072086, 'd13': 0.015788, 'd23': -0.053192},
        uncertainties = {'d12': 0.062556, 'd13': 0.072528, 'd23': 0.062176},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 30 distances.
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
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
        distances = {'d12': 0.104163, 'd13': 0.026373, 'd23': -0.080074},
        uncertainties = {'d12': 0.106797, 'd13': 0.08409, 'd23': 0.068949},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 79 distances.
[<Entry index=38 label="Cd/H/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=194 label="O2b">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=241 label="Cb_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=203 label="OOC">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=246 label="CO_rad/OneDe">]
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
        distances = {'d12': 0.033884, 'd13': 0.006386, 'd23': -0.029006},
        uncertainties = {'d12': 0.049813, 'd13': 0.028988, 'd23': 0.041099},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 26 distances.
[<Entry index=35 label="Cd/H/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=241 label="Cb_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=203 label="OOC">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=243 label="CO_pri_rad">]
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
        distances = {'d12': 0.139835, 'd13': 0.036518, 'd23': -0.105994},
        uncertainties = {'d12': 0.12747, 'd13': 0.101942, 'd23': 0.080459},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 53 distances.
[<Entry index=38 label="Cd/H/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=194 label="O2b">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
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
        distances = {'d12': 0.124436, 'd13': 0.033127, 'd23': -0.092331},
        uncertainties = {'d12': 0.088909, 'd13': 0.080396, 'd23': 0.072489},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 44 distances.
[<Entry index=40 label="Cb_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=40 label="Cb_H">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=40 label="Cb_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=40 label="Cb_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=261 label="C_methyl">]
[<Entry index=40 label="Cb_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=40 label="Cb_H">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=40 label="Cb_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=40 label="Cb_H">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=40 label="Cb_H">, <Entry index=192 label="H_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=40 label="Cb_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=203 label="OOC">]
[<Entry index=40 label="Cb_H">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=40 label="Cb_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=40 label="Cb_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=198 label="O_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=243 label="CO_pri_rad">]
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
        distances = {'d12': -0.001372, 'd13': 0.057711, 'd23': 0.059389},
        uncertainties = {'d12': 0.053442, 'd13': 0.050255, 'd23': 0.083716},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 153 distances.
[<Entry index=47 label="CO/H/OneDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=203 label="OOC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=42 label="CO_pri">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=42 label="CO_pri">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=42 label="CO_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=42 label="CO_pri">, <Entry index=203 label="OOC">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=203 label="OOC">]
[<Entry index=42 label="CO_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=42 label="CO_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=42 label="CO_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=192 label="H_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=190 label="CH2_triplet">]
[<Entry index=42 label="CO_pri">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=194 label="O2b">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=42 label="CO_pri">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=192 label="H_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=42 label="CO_pri">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=241 label="Cb_rad">]
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
        distances = {'d12': 0.000467, 'd13': 0.050841, 'd23': 0.049726},
        uncertainties = {'d12': 0.054937, 'd13': 0.045921, 'd23': 0.077487},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 50 distances.
[<Entry index=42 label="CO_pri">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=42 label="CO_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=42 label="CO_pri">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=42 label="CO_pri">, <Entry index=194 label="O2b">]
[<Entry index=42 label="CO_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=42 label="CO_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=42 label="CO_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=261 label="C_methyl">]
[<Entry index=42 label="CO_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=42 label="CO_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=42 label="CO_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=42 label="CO_pri">, <Entry index=192 label="H_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=42 label="CO_pri">, <Entry index=203 label="OOC">]
[<Entry index=42 label="CO_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=190 label="CH2_triplet">]
[<Entry index=42 label="CO_pri">, <Entry index=275 label="C_rad/H2/Cd">]
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
        distances = {'d12': -0.002287, 'd13': 0.061127, 'd23': 0.064195},
        uncertainties = {'d12': 0.05364, 'd13': 0.052976, 'd23': 0.087844},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 103 distances.
[<Entry index=47 label="CO/H/OneDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=236 label="Cd_rad/Ct">]
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
[<Entry index=45 label="CO/H/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=203 label="OOC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=241 label="Cb_rad">]
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
        distances = {'d12': -0.009196, 'd13': 0.062334, 'd23': 0.071787},
        uncertainties = {'d12': 0.057913, 'd13': 0.056518, 'd23': 0.099232},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 60 distances.
[<Entry index=45 label="CO/H/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=203 label="OOC">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=192 label="H_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
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
        distances = {'d12': -0.009637, 'd13': 0.067136, 'd23': 0.077298},
        uncertainties = {'d12': 0.055258, 'd13': 0.052979, 'd23': 0.090042},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 55 distances.
[<Entry index=45 label="CO/H/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=203 label="OOC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
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
        distances = {'d12': -0.03999, 'd13': 0.088998, 'd23': 0.127041},
        uncertainties = {'d12': 0.105078, 'd13': 0.02582, 'd23': 0.124666},
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
        distances = {'d12': 0.006808, 'd13': 0.059539, 'd23': 0.0542},
        uncertainties = {'d12': 0.049408, 'd13': 0.049911, 'd23': 0.073003},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 43 distances.
[<Entry index=47 label="CO/H/OneDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=261 label="C_methyl">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=203 label="OOC">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=241 label="Cb_rad">]
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
        distances = {'d12': 0.007461, 'd13': 0.032296, 'd23': 0.023642},
        uncertainties = {'d12': 0.051632, 'd13': 0.052906, 'd23': 0.06628},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1266 distances.
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=61 label="C_methane">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
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
[<Entry index=72 label="C/H3/O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=72 label="C/H3/O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=241 label="Cb_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=194 label="O2b">]
[<Entry index=61 label="C_methane">, <Entry index=374 label="C_rad/CdCdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=96 label="C/H2/O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
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
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=192 label="H_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=61 label="C_methane">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=241 label="Cb_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=194 label="O2b">]
[<Entry index=77 label="C/H3/CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=198 label="O_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=72 label="C/H3/O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=72 label="C/H3/O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=194 label="O2b">]
[<Entry index=77 label="C/H3/CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=245 label="CO_rad/NonDe">]
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
[<Entry index=94 label="C/H2/CsO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=194 label="O2b">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
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
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=241 label="Cb_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=67 label="C/H3/Cs\H2\Cs|O">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=192 label="H_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=241 label="Cb_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=61 label="C_methane">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=61 label="C_methane">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=241 label="Cb_rad">]
[<Entry index=61 label="C_methane">, <Entry index=198 label="O_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=203 label="OOC">]
[<Entry index=139 label="C/H/Cs2O">, <Entry index=192 label="H_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=194 label="O2b">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=192 label="H_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=241 label="Cb_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=178 label="C/H/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=203 label="OOC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=306 label="C_rad/H/OneDeO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=61 label="C_methane">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=241 label="Cb_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=192 label="H_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=325 label="C_rad/H/CdCd">]
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
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=241 label="Cb_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=236 label="Cd_rad/Ct">]
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
[<Entry index=94 label="C/H2/CsO">, <Entry index=190 label="CH2_triplet">]
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
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=241 label="Cb_rad">]
[<Entry index=61 label="C_methane">, <Entry index=203 label="OOC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=203 label="OOC">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=241 label="Cb_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=72 label="C/H3/O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=246 label="CO_rad/OneDe">]
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
[<Entry index=78 label="C/H3/Cd">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=61 label="C_methane">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
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
[<Entry index=105 label="C/H2/CdCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=194 label="O2b">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=192 label="H_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
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
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=198 label="O_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=96 label="C/H2/O2">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=108 label="C/H2/OneDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=203 label="OOC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=192 label="H_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=203 label="OOC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/O">, <Entry index=261 label="C_methyl">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=261 label="C_methyl">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=239 label="Cd_rad/Cd">]
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
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=236 label="Cd_rad/Ct">]
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
        distances = {'d12': 0.07668, 'd13': 0.028801, 'd23': -0.051468},
        uncertainties = {'d12': 0.061789, 'd13': 0.048866, 'd23': 0.044161},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 69 distances.
[<Entry index=61 label="C_methane">, <Entry index=241 label="Cb_rad">]
[<Entry index=61 label="C_methane">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=61 label="C_methane">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=374 label="C_rad/CdCdCs">]
[<Entry index=61 label="C_methane">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
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
        distances = {'d12': 0.025511, 'd13': 0.025031, 'd23': -0.00223},
        uncertainties = {'d12': 0.049389, 'd13': 0.04266, 'd23': 0.056327},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 684 distances.
[<Entry index=63 label="C/H3/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=194 label="O2b">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=241 label="Cb_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=198 label="O_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=203 label="OOC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=243 label="CO_pri_rad">]
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
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=306 label="C_rad/H/OneDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=72 label="C/H3/O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=77 label="C/H3/CO">, <Entry index=194 label="O2b">]
[<Entry index=72 label="C/H3/O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=192 label="H_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=72 label="C/H3/O">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=72 label="C/H3/O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=236 label="Cd_rad/Ct">]
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
[<Entry index=75 label="C/H3/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=192 label="H_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=203 label="OOC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=198 label="O_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=72 label="C/H3/O">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=72 label="C/H3/O">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=190 label="CH2_triplet">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=241 label="Cb_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=72 label="C/H3/O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=67 label="C/H3/Cs\H2\Cs|O">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=72 label="C/H3/O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=203 label="OOC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=203 label="OOC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=194 label="O2b">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=241 label="Cb_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=198 label="O_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=241 label="Cb_rad">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=72 label="C/H3/O">, <Entry index=261 label="C_methyl">]
[<Entry index=72 label="C/H3/O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=194 label="O2b">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=77 label="C/H3/CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=72 label="C/H3/O">, <Entry index=224 label="Cd_pri_rad">]
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
        distances = {'d12': 0.051887, 'd13': 0.021528, 'd23': -0.033063},
        uncertainties = {'d12': 0.046392, 'd13': 0.048146, 'd23': 0.056885},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 357 distances.
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=203 label="OOC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=306 label="C_rad/H/OneDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
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
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=241 label="Cb_rad">]
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
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=241 label="Cb_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=67 label="C/H3/Cs\H2\Cs|O">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=203 label="OOC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=203 label="OOC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=198 label="O_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=236 label="Cd_rad/Ct">]
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
        distances = {'d12': 0.04588, 'd13': 0.024181, 'd23': -0.025075},
        uncertainties = {'d12': 0.053579, 'd13': 0.036739, 'd23': 0.051754},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 65 distances.
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=198 label="O_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=306 label="C_rad/H/OneDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
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
        distances = {'d12': 0.053158, 'd13': 0.017928, 'd23': -0.03789},
        uncertainties = {'d12': 0.044192, 'd13': 0.06307, 'd23': 0.069242},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 107 distances.
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=198 label="O_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=241 label="Cb_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=67 label="C/H3/Cs\H2\Cs|O">, <Entry index=192 label="H_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=192 label="H_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=236 label="Cd_rad/Ct">]
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
        distances = {'d12': 0.049403, 'd13': 0.010665, 'd23': -0.042001},
        uncertainties = {'d12': 0.040016, 'd13': 0.075716, 'd23': 0.073518},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 59 distances.
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=67 label="C/H3/Cs\H2\Cs|O">, <Entry index=192 label="H_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=241 label="Cb_rad">]
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
        distances = {'d12': 0.045526, 'd13': -0.246802, 'd23': -0.296175},
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
        distances = {'d12': 0.057673, 'd13': 0.02666, 'd23': -0.032947},
        uncertainties = {'d12': 0.050389, 'd13': 0.045731, 'd23': 0.066305},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 48 distances.
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=198 label="O_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=241 label="Cb_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=203 label="OOC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=270 label="C_rad/H2/Ct">]
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
        distances = {'d12': 0.049381, 'd13': 0.021282, 'd23': -0.031488},
        uncertainties = {'d12': 0.046179, 'd13': 0.043861, 'd23': 0.053075},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 44 distances.
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=190 label="CH2_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=198 label="O_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=236 label="Cd_rad/Ct">]
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
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=239 label="Cd_rad/Cd">]
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
        distances = {'d12': 0.025187, 'd13': 0.020403, 'd23': 0.000259},
        uncertainties = {'d12': 0.045828, 'd13': 0.03303, 'd23': 0.051077},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 53 distances.
[<Entry index=72 label="C/H3/O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=72 label="C/H3/O">, <Entry index=236 label="Cd_rad/Ct">]
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
[<Entry index=72 label="C/H3/O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
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
[<Entry index=72 label="C/H3/O">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=241 label="Cb_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
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
        distances = {'d12': -0.007707, 'd13': 0.030303, 'd23': 0.036215},
        uncertainties = {'d12': 0.054203, 'd13': 0.036719, 'd23': 0.057213},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 274 distances.
[<Entry index=77 label="C/H3/CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=194 label="O2b">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=241 label="Cb_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=203 label="OOC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=194 label="O2b">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=194 label="O2b">]
[<Entry index=77 label="C/H3/CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=77 label="C/H3/CO">, <Entry index=192 label="H_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=261 label="C_methyl">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=190 label="CH2_triplet">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=77 label="C/H3/CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=273 label="C_rad/H2/O">]
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
[<Entry index=77 label="C/H3/CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=241 label="Cb_rad">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=203 label="OOC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
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
        distances = {'d12': -0.003456, 'd13': 0.023, 'd23': 0.024269},
        uncertainties = {'d12': 0.049121, 'd13': 0.033168, 'd23': 0.045375},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 36 distances.
[<Entry index=75 label="C/H3/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=194 label="O2b">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=190 label="CH2_triplet">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=203 label="OOC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=241 label="Cb_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=243 label="CO_pri_rad">]
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
        distances = {'d12': 0.012344, 'd13': 0.016124, 'd23': 0.003831},
        uncertainties = {'d12': 0.059144, 'd13': 0.036526, 'd23': 0.051952},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 84 distances.
[<Entry index=77 label="C/H3/CO">, <Entry index=194 label="O2b">]
[<Entry index=77 label="C/H3/CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=192 label="H_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=203 label="OOC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=202 label="O_rad/NonDeO">]
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
        distances = {'d12': -0.019271, 'd13': 0.039454, 'd23': 0.056043},
        uncertainties = {'d12': 0.053705, 'd13': 0.038344, 'd23': 0.063174},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 154 distances.
[<Entry index=78 label="C/H3/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=194 label="O2b">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=241 label="Cb_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=192 label="H_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=236 label="Cd_rad/Ct">]
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
        distances = {'d12': -0.02259, 'd13': 0.03129, 'd23': 0.051658},
        uncertainties = {'d12': 0.040991, 'd13': 0.032831, 'd23': 0.037509},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 46 distances.
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=241 label="Cb_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=239 label="Cd_rad/Cd">]
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
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=236 label="Cd_rad/Ct">]
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
        distances = {'d12': -0.047979, 'd13': 0.031408, 'd23': 0.07593},
        uncertainties = {'d12': 0.120287, 'd13': 0.162386, 'd23': 0.068445},
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
        distances = {'d12': -0.023917, 'd13': 0.010253, 'd23': 0.029891},
        uncertainties = {'d12': 0.060163, 'd13': 0.187136, 'd23': 0.125195},
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
        distances = {'d12': -0.026003, 'd13': 0.044341, 'd23': 0.069757},
        uncertainties = {'d12': 0.054585, 'd13': 0.065524, 'd23': 0.082419},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 409 distances.
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=261 label="C_methyl">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=194 label="O2b">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=203 label="OOC">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=241 label="Cb_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=261 label="C_methyl">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=241 label="Cb_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=192 label="H_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
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
[<Entry index=105 label="C/H2/CdCs">, <Entry index=241 label="Cb_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=261 label="C_methyl">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=192 label="H_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=194 label="O2b">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
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
[<Entry index=94 label="C/H2/CsO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=261 label="C_methyl">]
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
[<Entry index=103 label="C/H2/COCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=192 label="H_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=261 label="C_methyl">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=241 label="Cb_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=192 label="H_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=241 label="Cb_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
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
        distances = {'d12': 0.027438, 'd13': 0.010886, 'd23': -0.019733},
        uncertainties = {'d12': 0.05869, 'd13': 0.04024, 'd23': 0.05646},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 73 distances.
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
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
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=261 label="C_methyl">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
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
        distances = {'d12': -0.018316, 'd13': -0.027701, 'd23': -0.013568},
        uncertainties = {'d12': 0.074901, 'd13': 0.129617, 'd23': 0.060019},
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
        distances = {'d12': 0.037209, 'd13': 0.029214, 'd23': -0.011011},
        uncertainties = {'d12': 0.0577, 'd13': 0.034334, 'd23': 0.04928},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 53 distances.
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
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
        distances = {'d12': 0.011534, 'd13': 0.027527, 'd23': 0.020231},
        uncertainties = {'d12': 0.060052, 'd13': 0.038685, 'd23': 0.078311},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 52 distances.
[<Entry index=94 label="C/H2/CsO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=96 label="C/H2/O2">, <Entry index=261 label="C_methyl">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=261 label="C_methyl">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=96 label="C/H2/O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=192 label="H_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=241 label="Cb_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=275 label="C_rad/H2/Cd">]
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
        distances = {'d12': 0.010769, 'd13': 0.027966, 'd23': 0.021611},
        uncertainties = {'d12': 0.060185, 'd13': 0.039167, 'd23': 0.078518},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 50 distances.
[<Entry index=94 label="C/H2/CsO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=261 label="C_methyl">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=192 label="H_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=241 label="Cb_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=275 label="C_rad/H2/Cd">]
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
        distances = {'d12': 0.031818, 'd13': 0.015885, 'd23': -0.016339},
        uncertainties = {'d12': 0.521143, 'd13': 0.22835, 'd23': 0.671918},
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
        distances = {'d12': -0.037737, 'd13': 0.048927, 'd23': 0.086334},
        uncertainties = {'d12': 0.053546, 'd13': 0.067875, 'd23': 0.085427},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 185 distances.
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=241 label="Cb_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=261 label="C_methyl">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=108 label="C/H2/OneDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=194 label="O2b">]
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=236 label="Cd_rad/Ct">]
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
[<Entry index=105 label="C/H2/CdCs">, <Entry index=241 label="Cb_rad">]
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
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=290 label="C_rad/H/CsO">]
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
        distances = {'d12': -0.037603, 'd13': 0.048826, 'd23': 0.086091},
        uncertainties = {'d12': 0.05362, 'd13': 0.068055, 'd23': 0.085587},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 184 distances.
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=241 label="Cb_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=261 label="C_methyl">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=194 label="O2b">]
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=236 label="Cd_rad/Ct">]
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
[<Entry index=105 label="C/H2/CdCs">, <Entry index=241 label="Cb_rad">]
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
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=290 label="C_rad/H/CsO">]
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
        distances = {'d12': -0.014812, 'd13': 0.038405, 'd23': 0.053991},
        uncertainties = {'d12': 0.043624, 'd13': 0.039146, 'd23': 0.055515},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 41 distances.
[<Entry index=103 label="C/H2/COCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=241 label="Cb_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=261 label="C_methyl">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=192 label="H_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
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
        distances = {'d12': -0.050355, 'd13': 0.047057, 'd23': 0.09546},
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
        distances = {'d12': -0.043987, 'd13': 0.051745, 'd23': 0.095083},
        uncertainties = {'d12': 0.056627, 'd13': 0.074691, 'd23': 0.092984},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 143 distances.
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=194 label="O2b">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=200 label="O_rad/NonDeC">]
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
[<Entry index=105 label="C/H2/CdCs">, <Entry index=241 label="Cb_rad">]
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
        distances = {'d12': -0.029127, 'd13': 0.049531, 'd23': 0.076789},
        uncertainties = {'d12': 0.042289, 'd13': 0.056312, 'd23': 0.047875},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 33 distances.
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=241 label="Cb_rad">]
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
        distances = {'d12': -0.059511, 'd13': 0.065513, 'd23': 0.125879},
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
        distances = {'d12': -0.06037, 'd13': 0.067502, 'd23': 0.126094},
        uncertainties = {'d12': 0.053415, 'd13': 0.086745, 'd23': 0.097563},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 99 distances.
[<Entry index=127 label="C/H2/CdCd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
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
[<Entry index=127 label="C/H2/CdCd">, <Entry index=194 label="O2b">]
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
        distances = {'d12': -0.06037, 'd13': 0.067502, 'd23': 0.126094},
        uncertainties = {'d12': 0.053415, 'd13': 0.086745, 'd23': 0.097563},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 99 distances.
[<Entry index=127 label="C/H2/CdCd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
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
[<Entry index=127 label="C/H2/CdCd">, <Entry index=194 label="O2b">]
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
        distances = {'d12': -0.025676, 'd13': 0.034956, 'd23': 0.062321},
        uncertainties = {'d12': 0.049528, 'd13': 0.062854, 'd23': 0.070802},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 104 distances.
[<Entry index=133 label="C/H/Cs3">, <Entry index=194 label="O2b">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
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
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=192 label="H_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=241 label="Cb_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=192 label="H_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=139 label="C/H/Cs2O">, <Entry index=192 label="H_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
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
        distances = {'d12': 0.001573, 'd13': 0.006838, 'd23': 0.003478},
        uncertainties = {'d12': 0.061552, 'd13': 0.146892, 'd23': 0.132744},
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
        distances = {'d12': 0.006985, 'd13': 0.014344, 'd23': 0.005657},
        uncertainties = {'d12': 0.061698, 'd13': 0.056503, 'd23': 0.057519},
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
        distances = {'d12': -0.128313, 'd13': -0.173313, 'd23': -0.0488},
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
        distances = {'d12': -0.128313, 'd13': -0.173313, 'd23': -0.0488},
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
        distances = {'d12': -0.029273, 'd13': 0.038474, 'd23': 0.070037},
        uncertainties = {'d12': 0.047795, 'd13': 0.038369, 'd23': 0.056709},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 87 distances.
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=261 label="C_methyl">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=192 label="H_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
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
        distances = {'d12': -0.029273, 'd13': 0.038474, 'd23': 0.070037},
        uncertainties = {'d12': 0.047795, 'd13': 0.038369, 'd23': 0.056709},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 87 distances.
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=261 label="C_methyl">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=192 label="H_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
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
        distances = {'d12': -0.029273, 'd13': 0.038474, 'd23': 0.070037},
        uncertainties = {'d12': 0.047795, 'd13': 0.038369, 'd23': 0.056709},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 87 distances.
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=261 label="C_methyl">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=192 label="H_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
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
        distances = {'d12': -0.119337, 'd13': 0.154144, 'd23': 0.270561},
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
        distances = {'d12': -0.119337, 'd13': 0.154144, 'd23': 0.270561},
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
        distances = {'d12': -0.119337, 'd13': 0.154144, 'd23': 0.270561},
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
        distances = {'d12': 0.094987, 'd13': -0.00843, 'd23': -0.106435},
        uncertainties = {'d12': 0.096751, 'd13': 0.07818, 'd23': 0.073255},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 53 distances.
[<Entry index=443 label="OH_rad_H">, <Entry index=261 label="C_methyl">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=443 label="OH_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=192 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=443 label="OH_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=443 label="OH_rad_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=203 label="OOC">]
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
        distances = {'d12': 0.155959, 'd13': 0.041719, 'd23': -0.117206},
        uncertainties = {'d12': 0.091006, 'd13': 0.090865, 'd23': 0.044639},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 38 distances.
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=203 label="OOC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=192 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=290 label="C_rad/H/CsO">]
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
        distances = {'d12': 0.155959, 'd13': 0.041719, 'd23': -0.117206},
        uncertainties = {'d12': 0.091006, 'd13': 0.090865, 'd23': 0.044639},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 38 distances.
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=203 label="OOC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=192 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=290 label="C_rad/H/CsO">]
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
        distances = {'d12': -0.074639, 'd13': -0.147944, 'd23': -0.076468},
        uncertainties = {'d12': 0.123268, 'd13': 0.038544, 'd23': 0.129884},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 15 distances.
[<Entry index=443 label="OH_rad_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=443 label="OH_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=261 label="C_methyl">]
[<Entry index=443 label="OH_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
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
)

entry(
    index = 444,
    label = "Xbirad_H",
    group = "OR{CH2_triplet_H, CH2_singlet_H, NH_triplet_H, NH_singlet_H}",
    distances = DistanceData(distances={}),
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
)

entry(
    index = 474,
    label = "Xtrirad_H",
    group = "OR{C_quartet_H, C_doublet_H}",
    distances = DistanceData(distances={}),
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
)

entry(
    index = 475,
    label = "Y_1centerquadrad",
    group = "OR{C_quintet, C_triplet, C_singlet}",
    distances = DistanceData(distances={}),
)

entry(
    index = 482,
    label = "C_quintet",
    group = 
"""
1 *3 C u4
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 483,
    label = "C_triplet",
    group = 
"""
1 *3 C u4
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 484,
    label = "C_singlet",
    group = 
"""
1 *3 C u4
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 419,
    label = "Y_1centertrirad",
    group = "OR{N_atom_quartet, N_atom_doublet, CH_quartet, CH_doublet}",
    distances = DistanceData(distances={}),
)

entry(
    index = 485,
    label = "N_atom_quartet",
    group = 
"""
1 *3 N u3
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 486,
    label = "N_atom_doublet",
    group = 
"""
1 *3 N u3
""",
    distances = DistanceData(distances={}),
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
)

entry(
    index = 188,
    label = "Y_1centerbirad",
    group = 
"""
1 *3 [Cs,Cd,CO,CS,O,S,N] u2
""",
    distances = DistanceData(
        distances = {'d12': -0.106387, 'd13': -0.010316, 'd23': 0.093103},
        uncertainties = {'d12': 0.072578, 'd13': 0.077469, 'd23': 0.097783},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 53 distances.
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=72 label="C/H3/O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=190 label="CH2_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=72 label="C/H3/O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=189 label="O_atom_triplet">]
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
        distances = {'d12': -0.078856, 'd13': -0.149113, 'd23': -0.073302},
        uncertainties = {'d12': 0.126777, 'd13': 0.038514, 'd23': 0.121672},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 15 distances.
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=72 label="C/H3/O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=61 label="C_methane">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=189 label="O_atom_triplet">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=189 label="O_atom_triplet">]
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
        distances = {'d12': -0.116742, 'd13': 0.041886, 'd23': 0.155689},
        uncertainties = {'d12': 0.046048, 'd13': 0.089993, 'd23': 0.093282},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 38 distances.
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=72 label="C/H3/O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=190 label="CH2_triplet">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=190 label="CH2_triplet">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=190 label="CH2_triplet">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=77 label="C/H3/CO">, <Entry index=190 label="CH2_triplet">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=190 label="CH2_triplet">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=190 label="CH2_triplet">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=190 label="CH2_triplet">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=190 label="CH2_triplet">]
[<Entry index=11 label="H2O2">, <Entry index=190 label="CH2_triplet">]
[<Entry index=42 label="CO_pri">, <Entry index=190 label="CH2_triplet">]
[<Entry index=4 label="H2">, <Entry index=190 label="CH2_triplet">]
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
)

entry(
    index = 191,
    label = "Y_rad",
    group = 
"""
1 *3 R u1
""",
    distances = DistanceData(
        distances = {'d12': 0.002857, 'd13': 0.000277, 'd23': -0.0025},
        uncertainties = {'d12': 0.080192, 'd13': 0.066909, 'd23': 0.078552},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2089 distances.
[<Entry index=38 label="Cd/H/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=7 label="O_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=11 label="H2O2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=61 label="C_methane">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=4 label="H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=72 label="C/H3/O">, <Entry index=261 label="C_methyl">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
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
[<Entry index=443 label="OH_rad_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=192 label="H_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=42 label="CO_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=4 label="H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=261 label="C_methyl">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=61 label="C_methane">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=13 label="ROOH_sec">, <Entry index=194 label="O2b">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=241 label="Cb_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=194 label="O2b">]
[<Entry index=61 label="C_methane">, <Entry index=374 label="C_rad/CdCdCs">]
[<Entry index=4 label="H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=4 label="H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=16 label="Orad_O_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=40 label="Cb_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=241 label="Cb_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=96 label="C/H2/O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=42 label="CO_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=203 label="OOC">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=232 label="Cd_Cd\H\Cs_rad/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=272 label="C_rad/H2/CO">]
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
[<Entry index=38 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=203 label="OOC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=192 label="H_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=4 label="H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=4 label="H2">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=261 label="C_methyl">]
[<Entry index=72 label="C/H3/O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=42 label="CO_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=72 label="C/H3/O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=192 label="H_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=194 label="O2b">]
[<Entry index=61 label="C_methane">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=192 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=61 label="C_methane">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=261 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=273 label="C_rad/H2/O">]
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
[<Entry index=127 label="C/H2/CdCd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=7 label="O_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=198 label="O_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=443 label="OH_rad_H">, <Entry index=261 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=203 label="OOC">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=194 label="O2b">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=16 label="Orad_O_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=4 label="H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=443 label="OH_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=194 label="O2b">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/O">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=245 label="CO_rad/NonDe">]
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
[<Entry index=94 label="C/H2/CsO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=108 label="C/H2/OneDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=194 label="O2b">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
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
[<Entry index=35 label="Cd/H/Ct">, <Entry index=243 label="CO_pri_rad">]
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
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=241 label="Cb_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=67 label="C/H3/Cs\H2\Cs|O">, <Entry index=192 label="H_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=192 label="H_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=42 label="CO_pri">, <Entry index=192 label="H_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=241 label="Cb_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=42 label="CO_pri">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=61 label="C_methane">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=61 label="C_methane">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=192 label="H_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=198 label="O_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=261 label="C_methyl">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=192 label="H_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=241 label="Cb_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=72 label="C/H3/O">, <Entry index=203 label="OOC">]
[<Entry index=40 label="Cb_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=139 label="C/H/Cs2O">, <Entry index=192 label="H_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=192 label="H_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=241 label="Cb_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=11 label="H2O2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H2/Cs\H2\Cs|Cs#O">]
[<Entry index=42 label="CO_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=178 label="C/H/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=306 label="C_rad/H/OneDeO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=11 label="H2O2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=241 label="Cb_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=261 label="C_methyl">]
[<Entry index=42 label="CO_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=192 label="H_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=192 label="H_rad">]
[<Entry index=4 label="H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=40 label="Cb_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=236 label="Cd_rad/Ct">]
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
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=192 label="H_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=241 label="Cb_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=72 label="C/H3/O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=42 label="CO_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=273 label="C_rad/H2/O">]
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
[<Entry index=16 label="Orad_O_H">, <Entry index=239 label="Cd_rad/Cd">]
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
[<Entry index=35 label="Cd/H/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=335 label="C_rad/Cs2O">]
[<Entry index=7 label="O_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
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
[<Entry index=105 label="C/H2/CdCs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=14 label="ROOH_ter">, <Entry index=261 label="C_methyl">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=241 label="Cb_rad">]
[<Entry index=61 label="C_methane">, <Entry index=203 label="OOC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=203 label="OOC">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=241 label="Cb_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=192 label="H_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=40 label="Cb_H">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=241 label="Cb_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=198 label="O_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=16 label="Orad_O_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
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
[<Entry index=40 label="Cb_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=11 label="H2O2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=203 label="OOC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
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
[<Entry index=105 label="C/H2/CdCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=192 label="H_rad">]
[<Entry index=61 label="C_methane">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=194 label="O2b">]
[<Entry index=443 label="OH_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=192 label="H_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=290 label="C_rad/H/CsO">]
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
[<Entry index=47 label="CO/H/OneDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=454 label="O/H/OneDeC">, <Entry index=192 label="H_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=261 label="C_methyl">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=61 label="C_methane">, <Entry index=198 label="O_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=61 label="C_methane">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=198 label="O_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=96 label="C/H2/O2">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=261 label="C_methyl">]
[<Entry index=4 label="H2">, <Entry index=491 label="O_rad/OneDeC">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=61 label="C_methane">, <Entry index=192 label="H_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=203 label="OOC">]
[<Entry index=42 label="CO_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=192 label="H_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=203 label="OOC">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=203 label="OOC">]
[<Entry index=16 label="Orad_O_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=192 label="H_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=194 label="O2b">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=192 label="H_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=7 label="O_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=192 label="H_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=239 label="Cd_rad/Cd">]
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
[<Entry index=42 label="CO_pri">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=40 label="Cb_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=61 label="C_methane">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=11 label="H2O2">, <Entry index=243 label="CO_pri_rad">]
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
        distances = {'d12': -0.04416, 'd13': -0.371926, 'd23': -0.330263},
        uncertainties = {'d12': 0.113317, 'd13': 0.129189, 'd23': 0.172327},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 70 distances.
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
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=192 label="H_rad">]
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
        distances = {'d12': 0.183054, 'd13': -0.063414, 'd23': -0.24477},
        uncertainties = {'d12': 0.138334, 'd13': 0.095215, 'd23': 0.101021},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 22 distances.
[<Entry index=133 label="C/H/Cs3">, <Entry index=194 label="O2b">]
[<Entry index=42 label="CO_pri">, <Entry index=194 label="O2b">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=77 label="C/H3/CO">, <Entry index=194 label="O2b">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=72 label="C/H3/O">, <Entry index=194 label="O2b">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=194 label="O2b">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=194 label="O2b">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=194 label="O2b">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=194 label="O2b">]
[<Entry index=12 label="ROOH_pri">, <Entry index=194 label="O2b">]
[<Entry index=13 label="ROOH_sec">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=194 label="O2b">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=194 label="O2b">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=194 label="O2b">]
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
        distances = {'d12': 0.183054, 'd13': -0.063414, 'd23': -0.24477},
        uncertainties = {'d12': 0.138334, 'd13': 0.095215, 'd23': 0.101021},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 22 distances.
[<Entry index=133 label="C/H/Cs3">, <Entry index=194 label="O2b">]
[<Entry index=42 label="CO_pri">, <Entry index=194 label="O2b">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=194 label="O2b">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=77 label="C/H3/CO">, <Entry index=194 label="O2b">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=194 label="O2b">]
[<Entry index=72 label="C/H3/O">, <Entry index=194 label="O2b">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=194 label="O2b">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=194 label="O2b">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=194 label="O2b">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=194 label="O2b">]
[<Entry index=12 label="ROOH_pri">, <Entry index=194 label="O2b">]
[<Entry index=13 label="ROOH_sec">, <Entry index=194 label="O2b">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=194 label="O2b">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=194 label="O2b">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=194 label="O2b">]
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
        distances = {'d12': -0.215601, 'd13': 0.121746, 'd23': 0.427396},
        uncertainties = {'d12': 0.159814, 'd13': 0.202782, 'd23': 0.198802},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 12 distances.
[<Entry index=105 label="C/H2/CdCs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
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
        distances = {'d12': -0.215601, 'd13': 0.121746, 'd23': 0.427396},
        uncertainties = {'d12': 0.159814, 'd13': 0.202782, 'd23': 0.198802},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 12 distances.
[<Entry index=105 label="C/H2/CdCs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=423 label="Ct_rad/Ct">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=423 label="Ct_rad/Ct">]
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
        distances = {'d12': -0.035877, 'd13': -0.148471, 'd23': -0.108766},
        uncertainties = {'d12': 0.100986, 'd13': 0.075747, 'd23': 0.097948},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 203 distances.
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=198 label="O_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=4 label="H2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=203 label="OOC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=203 label="OOC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=203 label="OOC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=203 label="OOC">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=203 label="OOC">]
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
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=202 label="O_rad/NonDeO">]
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
[<Entry index=47 label="CO/H/OneDe">, <Entry index=200 label="O_rad/NonDeC">]
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
        distances = {'d12': -0.200121, 'd13': -0.153831, 'd23': 0.080838},
        uncertainties = {'d12': 0.065486, 'd13': 0.171784, 'd23': 0.181077},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 14 distances.
[<Entry index=4 label="H2">, <Entry index=198 label="O_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=198 label="O_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=198 label="O_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=198 label="O_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=198 label="O_pri_rad">]
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
        distances = {'d12': -0.02499, 'd13': -0.148115, 'd23': -0.121335},
        uncertainties = {'d12': 0.103538, 'd13': 0.066851, 'd23': 0.091799},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 189 distances.
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=203 label="OOC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=203 label="OOC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=203 label="OOC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=203 label="OOC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=203 label="OOC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=203 label="OOC">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=203 label="OOC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=203 label="OOC">]
[<Entry index=42 label="CO_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=203 label="OOC">]
[<Entry index=61 label="C_methane">, <Entry index=203 label="OOC">]
[<Entry index=42 label="CO_pri">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=202 label="O_rad/NonDeO">]
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
[<Entry index=63 label="C/H3/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=203 label="OOC">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=200 label="O_rad/NonDeC">]
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
[<Entry index=47 label="CO/H/OneDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=203 label="OOC">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=203 label="OOC">]
[<Entry index=61 label="C_methane">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=203 label="OOC">]
[<Entry index=16 label="Orad_O_H">, <Entry index=203 label="OOC">]
[<Entry index=40 label="Cb_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=203 label="OOC">]
[<Entry index=7 label="O_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=203 label="OOC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=72 label="C/H3/O">, <Entry index=203 label="OOC">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=61 label="C_methane">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=200 label="O_rad/NonDeC">]
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
        distances = {'d12': -0.091751, 'd13': -0.156592, 'd23': -0.061514},
        uncertainties = {'d12': 0.052599, 'd13': 0.068959, 'd23': 0.068484},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 51 distances.
[<Entry index=63 label="C/H3/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=42 label="CO_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=7 label="O_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=4 label="H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=77 label="C/H3/CO">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=200 label="O_rad/NonDeC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=200 label="O_rad/NonDeC">]
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
        distances = {'d12': 0.000232, 'd13': -0.144048, 'd23': -0.143066},
        uncertainties = {'d12': 0.112014, 'd13': 0.052575, 'd23': 0.100039},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 137 distances.
[<Entry index=133 label="C/H/Cs3">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=203 label="OOC">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=203 label="OOC">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=203 label="OOC">]
[<Entry index=16 label="Orad_O_H">, <Entry index=203 label="OOC">]
[<Entry index=40 label="Cb_H">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=203 label="OOC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=203 label="OOC">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=203 label="OOC">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=203 label="OOC">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=203 label="OOC">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=7 label="O_pri">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=202 label="O_rad/NonDeO">]
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
[<Entry index=77 label="C/H3/CO">, <Entry index=203 label="OOC">]
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
[<Entry index=47 label="CO/H/OneDe">, <Entry index=203 label="OOC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=203 label="OOC">]
[<Entry index=40 label="Cb_H">, <Entry index=203 label="OOC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=203 label="OOC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=203 label="OOC">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=203 label="OOC">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=202 label="O_rad/NonDeO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=203 label="OOC">]
[<Entry index=72 label="C/H3/O">, <Entry index=203 label="OOC">]
[<Entry index=42 label="CO_pri">, <Entry index=202 label="O_rad/NonDeO">]
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
        distances = {'d12': -0.00995, 'd13': -0.144316, 'd23': -0.133086},
        uncertainties = {'d12': 0.111217, 'd13': 0.045916, 'd23': 0.108676},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 100 distances.
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
[<Entry index=35 label="Cd/H/Ct">, <Entry index=203 label="OOC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=203 label="OOC">]
[<Entry index=40 label="Cb_H">, <Entry index=203 label="OOC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=203 label="OOC">]
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
        distances = {'d12': -0.139436, 'd13': -0.384069, 'd23': -0.241161},
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
        distances = {'d12': -0.139436, 'd13': -0.384069, 'd23': -0.241161},
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
        distances = {'d12': -0.068341, 'd13': 0.01772, 'd23': 0.08568},
        uncertainties = {'d12': 0.095469, 'd13': 0.085398, 'd23': 0.115778},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 319 distances.
[<Entry index=77 label="C/H3/CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=7 label="O_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=232 label="Cd_Cd\H\Cs_rad/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=61 label="C_methane">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=7 label="O_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=443 label="OH_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=443 label="OH_rad_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=236 label="Cd_rad/Ct">]
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
        distances = {'d12': -0.065901, 'd13': 0.014975, 'd23': 0.080755},
        uncertainties = {'d12': 0.104056, 'd13': 0.082129, 'd23': 0.125545},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 210 distances.
[<Entry index=4 label="H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
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
[<Entry index=40 label="Cb_H">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=443 label="OH_rad_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=224 label="Cd_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=224 label="Cd_pri_rad">]
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
        distances = {'d12': -0.090673, 'd13': 0.024431, 'd23': 0.111803},
        uncertainties = {'d12': 0.056516, 'd13': 0.075542, 'd23': 0.073545},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 37 distances.
[<Entry index=4 label="H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=7 label="O_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=11 label="H2O2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=225 label="Cd_Cd\H2_pri_rad">]
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
        distances = {'d12': -0.084518, 'd13': 0.030054, 'd23': 0.116254},
        uncertainties = {'d12': 0.065431, 'd13': 0.095475, 'd23': 0.093643},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 25 distances.
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=226 label="Cd_Cd\H\Cs_pri_rad">]
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
        distances = {'d12': -0.073073, 'd13': 0.023044, 'd23': 0.09523},
        uncertainties = {'d12': 0.07782, 'd13': 0.092734, 'd23': 0.09605},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 109 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=4 label="H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=4 label="H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=443 label="OH_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=232 label="Cd_Cd\H\Cs_rad/Cs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
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
        distances = {'d12': -0.053245, 'd13': 0.015883, 'd23': 0.071823},
        uncertainties = {'d12': 0.103184, 'd13': 0.119252, 'd23': 0.063117},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 30 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=4 label="H2">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=4 label="H2">, <Entry index=232 label="Cd_Cd\H\Cs_rad/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
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
        distances = {'d12': -0.047865, 'd13': 0.020717, 'd23': 0.071398},
        uncertainties = {'d12': 0.063058, 'd13': 0.075213, 'd23': 0.063206},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 29 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=4 label="H2">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=231 label="Cd_Cd\H2_rad/Cs">]
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
        distances = {'d12': -0.338387, 'd13': -0.240337, 'd23': 0.094328},
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
        distances = {'d12': -0.080561, 'd13': 0.025748, 'd23': 0.104069},
        uncertainties = {'d12': 0.068615, 'd13': 0.083676, 'd23': 0.107157},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 79 distances.
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=4 label="H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=443 label="OH_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
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
        distances = {'d12': -0.02843, 'd13': 0.006395, 'd23': 0.033281},
        uncertainties = {'d12': 0.040777, 'd13': 0.030135, 'd23': 0.049226},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 26 distances.
[<Entry index=42 label="CO_pri">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=72 label="C/H3/O">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=4 label="H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=236 label="Cd_rad/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=236 label="Cd_rad/Ct">]
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
        distances = {'d12': -0.106627, 'd13': 0.035425, 'd23': 0.139463},
        uncertainties = {'d12': 0.080097, 'd13': 0.101269, 'd23': 0.128033},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 53 distances.
[<Entry index=75 label="C/H3/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=4 label="H2">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=239 label="Cd_rad/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=239 label="Cd_rad/Cd">]
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
        distances = {'d12': -0.092544, 'd13': 0.033389, 'd23': 0.12482},
        uncertainties = {'d12': 0.069097, 'd13': 0.079949, 'd23': 0.087124},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 44 distances.
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=61 label="C_methane">, <Entry index=241 label="Cb_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=241 label="Cb_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=77 label="C/H3/CO">, <Entry index=241 label="Cb_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=241 label="Cb_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=241 label="Cb_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=241 label="Cb_rad">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=241 label="Cb_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=241 label="Cb_rad">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=241 label="Cb_rad">]
[<Entry index=11 label="H2O2">, <Entry index=241 label="Cb_rad">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=241 label="Cb_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=241 label="Cb_rad">]
[<Entry index=7 label="O_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=241 label="Cb_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=241 label="Cb_rad">]
[<Entry index=4 label="H2">, <Entry index=241 label="Cb_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=241 label="Cb_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=241 label="Cb_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=241 label="Cb_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=241 label="Cb_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=241 label="Cb_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=241 label="Cb_rad">]
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
        distances = {'d12': 0.06069, 'd13': 0.058483, 'd23': -0.00193},
        uncertainties = {'d12': 0.082879, 'd13': 0.051657, 'd23': 0.053698},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 153 distances.
[<Entry index=40 label="Cb_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=42 label="CO_pri">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=40 label="Cb_H">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=42 label="CO_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=4 label="H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=61 label="C_methane">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=16 label="Orad_O_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=72 label="C/H3/O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=61 label="C_methane">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=243 label="CO_pri_rad">]
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
        distances = {'d12': 0.051903, 'd13': 0.051657, 'd23': -0.000963},
        uncertainties = {'d12': 0.078243, 'd13': 0.047418, 'd23': 0.056866},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 50 distances.
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=61 label="C_methane">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=12 label="ROOH_pri">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=243 label="CO_pri_rad">]
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
[<Entry index=38 label="Cd/H/Cd">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=243 label="CO_pri_rad">]
[<Entry index=40 label="Cb_H">, <Entry index=243 label="CO_pri_rad">]
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
        distances = {'d12': 0.064999, 'd13': 0.061831, 'd23': -0.002404},
        uncertainties = {'d12': 0.086324, 'd13': 0.054367, 'd23': 0.05308},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 103 distances.
[<Entry index=40 label="Cb_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=42 label="CO_pri">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=4 label="H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=40 label="Cb_H">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=61 label="C_methane">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=61 label="C_methane">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=246 label="CO_rad/OneDe">]
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
[<Entry index=35 label="Cd/H/Ct">, <Entry index=245 label="CO_rad/NonDe">]
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
        distances = {'d12': 0.072193, 'd13': 0.063342, 'd23': -0.008661},
        uncertainties = {'d12': 0.097844, 'd13': 0.058846, 'd23': 0.056556},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 60 distances.
[<Entry index=40 label="Cb_H">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=245 label="CO_rad/NonDe">]
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
[<Entry index=38 label="Cd/H/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=11 label="H2O2">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=245 label="CO_rad/NonDe">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=245 label="CO_rad/NonDe">]
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
        distances = {'d12': 0.055533, 'd13': 0.059842, 'd23': 0.00583},
        uncertainties = {'d12': 0.071098, 'd13': 0.049829, 'd23': 0.050128},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 43 distances.
[<Entry index=63 label="C/H3/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=40 label="Cb_H">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=61 label="C_methane">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=77 label="C/H3/CO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=11 label="H2O2">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=12 label="ROOH_pri">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=72 label="C/H3/O">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=246 label="CO_rad/OneDe">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=246 label="CO_rad/OneDe">]
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
        distances = {'d12': 0.0242, 'd13': 0.032625, 'd23': 0.007289},
        uncertainties = {'d12': 0.068032, 'd13': 0.053338, 'd23': 0.052434},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1266 distances.
[<Entry index=38 label="Cd/H/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
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
[<Entry index=443 label="OH_rad_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=7 label="O_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=72 label="C/H3/O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
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
[<Entry index=38 label="Cd/H/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
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
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=42 label="CO_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=261 label="C_methyl">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=81 label="C/H3/Cd\Cs_Cd\H2">, <Entry index=261 label="C_methyl">]
[<Entry index=42 label="CO_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=270 label="C_rad/H2/Ct">]
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
[<Entry index=35 label="Cd/H/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=4 label="H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=61 label="C_methane">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=325 label="C_rad/H/CdCd">]
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
[<Entry index=94 label="C/H2/CsO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=261 label="C_methyl">]
[<Entry index=11 label="H2O2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=11 label="H2O2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=40 label="Cb_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=11 label="H2O2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=273 label="C_rad/H2/O">]
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
[<Entry index=35 label="Cd/H/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=261 label="C_methyl">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=108 label="C/H2/OneDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
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
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=40 label="Cb_H">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=261 label="C_methyl">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=261 label="C_methyl">]
[<Entry index=61 label="C_methane">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=261 label="C_methyl">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=272 label="C_rad/H2/CO">]
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
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=263 label="C_rad/H2/Cs">]
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
[<Entry index=9 label="O/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=4 label="H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=40 label="Cb_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
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
[<Entry index=35 label="Cd/H/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=61 label="C_methane">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=44 label="CO/H/NonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=84 label="C/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=104 label="C/H2/CO\H/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=273 label="C_rad/H2/O">]
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
[<Entry index=35 label="Cd/H/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
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
[<Entry index=103 label="C/H2/COCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=261 label="C_methyl">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=4 label="H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=40 label="Cb_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=16 label="Orad_O_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=11 label="H2O2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=72 label="C/H3/O">, <Entry index=261 label="C_methyl">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
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
[<Entry index=35 label="Cd/H/Ct">, <Entry index=290 label="C_rad/H/CsO">]
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
[<Entry index=442 label="CH3_rad_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=96 label="C/H2/O2">, <Entry index=261 label="C_methyl">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
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
[<Entry index=75 label="C/H3/Ct">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=16 label="Orad_O_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=261 label="C_methyl">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
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
[<Entry index=38 label="Cd/H/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
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
        distances = {'d12': -0.050813, 'd13': 0.028607, 'd23': 0.075919},
        uncertainties = {'d12': 0.045618, 'd13': 0.042411, 'd23': 0.06101},
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
        distances = {'d12': -0.001792, 'd13': 0.025176, 'd23': 0.025273},
        uncertainties = {'d12': 0.057411, 'd13': 0.044375, 'd23': 0.050321},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 684 distances.
[<Entry index=38 label="Cd/H/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=40 label="Cb_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=7 label="O_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=61 label="C_methane">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=4 label="H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=270 label="C_rad/H2/Ct">]
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
[<Entry index=35 label="Cd/H/Ct">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=16 label="Orad_O_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=16 label="Orad_O_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=61 label="C_methane">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=40 label="Cb_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=72 label="C/H3/O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
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
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
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
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=443 label="OH_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=72 label="C/H3/O">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=61 label="C_methane">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=272 label="C_rad/H2/CO">]
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
[<Entry index=40 label="Cb_H">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=12 label="ROOH_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=272 label="C_rad/H2/CO">]
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
[<Entry index=35 label="Cd/H/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=61 label="C_methane">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=40 label="Cb_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=72 label="C/H3/O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=61 label="C_methane">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=275 label="C_rad/H2/Cd">]
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
        distances = {'d12': -0.032772, 'd13': 0.021617, 'd23': 0.051719},
        uncertainties = {'d12': 0.057985, 'd13': 0.049824, 'd23': 0.048495},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 357 distances.
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=7 label="O_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=4 label="H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=4 label="H2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=87 label="C/H2/NonDeC_5ring">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=269 label="C_rad/H2/Cs\H2\Cs|Cs#O">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=7 label="O_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=72 label="C/H3/O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=40 label="Cb_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=40 label="Cb_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
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
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
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
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=61 label="C_methane">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=46 label="CO/H/Cs\Cs|Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=263 label="C_rad/H2/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=61 label="C_methane">, <Entry index=265 label="C_rad/H2/Cs\Cs2\O">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
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
        distances = {'d12': -0.024753, 'd13': 0.024509, 'd23': 0.045959},
        uncertainties = {'d12': 0.052999, 'd13': 0.039219, 'd23': 0.054943},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 65 distances.
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
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=96 label="C/H2/O2">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=12 label="ROOH_pri">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=61 label="C_methane">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=264 label="C_rad/H2/Cs\H3">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=264 label="C_rad/H2/Cs\H3">]
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
        distances = {'d12': -0.125966, 'd13': -0.097425, 'd23': 0.025305},
        uncertainties = {'d12': 1.09803, 'd13': 1.75099, 'd23': 0.763595},
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
        distances = {'d12': -0.033915, 'd13': 0.024538, 'd23': 0.05701},
        uncertainties = {'d12': 0.058274, 'd13': 0.054967, 'd23': 0.046158},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 31 distances.
[<Entry index=4 label="H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=42 label="CO_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=72 label="C/H3/O">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=11 label="H2O2">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=61 label="C_methane">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=266 label="C_rad/H2/Cs\H\Cs\Cs|O">]
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
        distances = {'d12': -0.29645, 'd13': -0.257321, 'd23': 0.035505},
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
        distances = {'d12': 0.02603, 'd13': 0.023289, 'd23': -0.004893},
        uncertainties = {'d12': 0.044652, 'd13': 0.034261, 'd23': 0.04737},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 36 distances.
[<Entry index=38 label="Cd/H/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=4 label="H2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=77 label="C/H3/CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=42 label="CO_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=12 label="ROOH_pri">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=40 label="Cb_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=16 label="Orad_O_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=72 label="C/H3/O">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=11 label="H2O2">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=270 label="C_rad/H2/Ct">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=270 label="C_rad/H2/Ct">]
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
        distances = {'d12': 0.004886, 'd13': 0.016257, 'd23': 0.011458},
        uncertainties = {'d12': 0.052014, 'd13': 0.038087, 'd23': 0.056445},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 84 distances.
[<Entry index=10 label="O/H/NonDeO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=42 label="CO_pri">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=40 label="Cb_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=443 label="OH_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=16 label="Orad_O_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=4 label="H2">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=272 label="C_rad/H2/CO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=272 label="C_rad/H2/CO">]
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
[<Entry index=35 label="Cd/H/Ct">, <Entry index=272 label="C_rad/H2/CO">]
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
        distances = {'d12': 0.000911, 'd13': 0.020406, 'd23': 0.024796},
        uncertainties = {'d12': 0.056298, 'd13': 0.035543, 'd23': 0.050748},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 53 distances.
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
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=11 label="H2O2">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=443 label="OH_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=12 label="ROOH_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=77 label="C/H3/CO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=42 label="CO_pri">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=273 label="C_rad/H2/O">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=273 label="C_rad/H2/O">]
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
        distances = {'d12': 0.056969, 'd13': 0.039836, 'd23': -0.019724},
        uncertainties = {'d12': 0.063857, 'd13': 0.040297, 'd23': 0.053689},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 154 distances.
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=275 label="C_rad/H2/Cd">]
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
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=77 label="C/H3/CO">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=61 label="C_methane">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=11 label="H2O2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=40 label="Cb_H">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=77 label="C/H3/CO">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=42 label="CO_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=16 label="Orad_O_H">, <Entry index=277 label="C_rad/H2/Cd\Cs_Cd\H2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
[<Entry index=4 label="H2">, <Entry index=275 label="C_rad/H2/Cd">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=275 label="C_rad/H2/Cd">]
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
        distances = {'d12': 0.058876, 'd13': 0.040298, 'd23': -0.021124},
        uncertainties = {'d12': 0.069189, 'd13': 0.040809, 'd23': 0.058753},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 118 distances.
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
[<Entry index=38 label="Cd/H/Cd">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
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
[<Entry index=35 label="Cd/H/Ct">, <Entry index=276 label="C_rad/H2/Cd\H_Cd\H2">]
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
        distances = {'d12': 0.030025, 'd13': 0.010083, 'd23': -0.02419},
        uncertainties = {'d12': 0.125475, 'd13': 0.18866, 'd23': 0.061027},
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
        distances = {'d12': 0.07055, 'd13': 0.044984, 'd23': -0.026112},
        uncertainties = {'d12': 0.086082, 'd13': 0.065363, 'd23': 0.056144},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 409 distances.
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
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
[<Entry index=40 label="Cb_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=443 label="OH_rad_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=133 label="C/H/Cs3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=306 label="C_rad/H/OneDeO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=61 label="C_methane">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=12 label="ROOH_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=11 label="H2O2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=11 label="H2O2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=443 label="OH_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=11 label="H2O2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=61 label="C_methane">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=42 label="CO_pri">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=16 label="Orad_O_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=61 label="C_methane">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=40 label="Cb_H">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=16 label="Orad_O_H">, <Entry index=325 label="C_rad/H/CdCd">]
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
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
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
        distances = {'d12': -0.018369, 'd13': 0.011442, 'd23': 0.026681},
        uncertainties = {'d12': 0.061495, 'd13': 0.035506, 'd23': 0.062506},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 73 distances.
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=61 label="C_methane">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=40 label="Cb_H">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=280 label="C_rad/H/NonDeC">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
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
        distances = {'d12': -0.010088, 'd13': 0.028957, 'd23': 0.036102},
        uncertainties = {'d12': 0.052856, 'd13': 0.034817, 'd23': 0.061012},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 53 distances.
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=77 label="C/H3/CO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=11 label="H2O2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=42 label="CO_pri">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=72 label="C/H3/O">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=4 label="H2">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=443 label="OH_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=283 label="C_rad/H/Cs\H3/Cs\H3">]
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
        distances = {'d12': 0.02031, 'd13': 0.027769, 'd23': 0.011913},
        uncertainties = {'d12': 0.081411, 'd13': 0.039238, 'd23': 0.064639},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 52 distances.
[<Entry index=10 label="O/H/NonDeO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=61 label="C_methane">, <Entry index=294 label="C_rad/H/O2">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=61 label="C_methane">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=72 label="C/H3/O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=40 label="Cb_H">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
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
        distances = {'d12': 0.021612, 'd13': 0.02819, 'd23': 0.011204},
        uncertainties = {'d12': 0.081724, 'd13': 0.039728, 'd23': 0.064939},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 50 distances.
[<Entry index=78 label="C/H3/Cd">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=77 label="C/H3/CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=42 label="CO_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=12 label="ROOH_pri">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=61 label="C_methane">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=72 label="C/H3/O">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=40 label="Cb_H">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=4 label="H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=11 label="H2O2">, <Entry index=290 label="C_rad/H/CsO">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=290 label="C_rad/H/CsO">]
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
        distances = {'d12': -0.016152, 'd13': 0.015998, 'd23': 0.03178},
        uncertainties = {'d12': 0.67599, 'd13': 0.23151, 'd23': 0.5242},
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
        distances = {'d12': 0.086671, 'd13': 0.04941, 'd23': -0.037595},
        uncertainties = {'d12': 0.089967, 'd13': 0.068576, 'd23': 0.054313},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 185 distances.
[<Entry index=75 label="C/H3/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
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
[<Entry index=38 label="Cd/H/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=40 label="Cb_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=306 label="C_rad/H/OneDeO">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=11 label="H2O2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
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
        distances = {'d12': 0.086442, 'd13': 0.049316, 'd23': -0.037467},
        uncertainties = {'d12': 0.090145, 'd13': 0.068758, 'd23': 0.05439},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 184 distances.
[<Entry index=75 label="C/H3/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
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
[<Entry index=38 label="Cd/H/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=4 label="H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=40 label="Cb_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=80 label="C/H3/Cd\H_Cd\H\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=72 label="C/H3/O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=103 label="C/H2/COCs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=11 label="H2O2">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
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
        distances = {'d12': 0.053933, 'd13': 0.038508, 'd23': -0.014722},
        uncertainties = {'d12': 0.056199, 'd13': 0.039687, 'd23': 0.043746},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 41 distances.
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=42 label="CO_pri">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=78 label="C/H3/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=61 label="C_methane">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=79 label="C/H3/Cd\H_Cd\H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=443 label="OH_rad_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=40 label="Cb_H">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=72 label="C/H3/O">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=303 label="C_rad/H/CO\H/Cs\H3">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=4 label="H2">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=302 label="C_rad/H/CO/Cs">]
[<Entry index=11 label="H2O2">, <Entry index=302 label="C_rad/H/CO/Cs">]
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
        distances = {'d12': 0.095705, 'd13': 0.047214, 'd23': -0.050407},
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
        distances = {'d12': 0.095805, 'd13': 0.052429, 'd23': -0.044019},
        uncertainties = {'d12': 0.098294, 'd13': 0.075443, 'd23': 0.057544},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 143 distances.
[<Entry index=75 label="C/H3/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=457 label="Ct/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=16 label="Orad_O_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=77 label="C/H3/CO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=35 label="Cd/H/Ct">, <Entry index=304 label="C_rad/H/CdCs">]
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
[<Entry index=45 label="CO/H/Cs">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=127 label="C/H2/CdCd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=42 label="CO_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=442 label="CH3_rad_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=12 label="ROOH_pri">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=40 label="Cb_H">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=61 label="C_methane">, <Entry index=304 label="C_rad/H/CdCs">]
[<Entry index=11 label="H2O2">, <Entry index=304 label="C_rad/H/CdCs">]
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
        distances = {'d12': 0.126124, 'd13': 0.06567, 'd23': -0.059563},
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
        distances = {'d12': 0.12691, 'd13': 0.068401, 'd23': -0.060266},
        uncertainties = {'d12': 0.099701, 'd13': 0.086559, 'd23': 0.052925},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 99 distances.
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=42 label="CO_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=61 label="C_methane">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=40 label="Cb_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=325 label="C_rad/H/CdCd">]
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
        distances = {'d12': 0.12691, 'd13': 0.068401, 'd23': -0.060266},
        uncertainties = {'d12': 0.099701, 'd13': 0.086559, 'd23': 0.052925},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 99 distances.
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=42 label="CO_pri">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=4 label="H2">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=68 label="C/H3/Cs\H2\O">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=61 label="C_methane">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=38 label="Cd/H/Cd">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=40 label="Cb_H">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=325 label="C_rad/H/CdCd">]
[<Entry index=16 label="Orad_O_H">, <Entry index=325 label="C_rad/H/CdCd">]
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
        distances = {'d12': 0.062942, 'd13': 0.035402, 'd23': -0.025701},
        uncertainties = {'d12': 0.067513, 'd13': 0.063139, 'd23': 0.047322},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 104 distances.
[<Entry index=69 label="C/H3/Cs\TwoNonDe">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=4 label="H2">, <Entry index=335 label="C_rad/Cs2O">]
[<Entry index=16 label="Orad_O_H">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=11 label="H2O2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=92 label="C/H2/Cs\H3/Cs\H3">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=61 label="C_methane">, <Entry index=374 label="C_rad/CdCdCs">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=42 label="CO_pri">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=61 label="C_methane">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=348 label="C_rad/COCs2">]
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
[<Entry index=12 label="ROOH_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=63 label="C/H3/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=330 label="C_rad/Cs3">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
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
        distances = {'d12': 0.005813, 'd13': 0.008314, 'd23': 0.00099},
        uncertainties = {'d12': 0.132171, 'd13': 0.1465, 'd23': 0.066504},
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
        distances = {'d12': 0.007964, 'd13': 0.015416, 'd23': 0.006028},
        uncertainties = {'d12': 0.058457, 'd13': 0.057374, 'd23': 0.066953},
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
        distances = {'d12': -0.049406, 'd13': -0.173976, 'd23': -0.128339},
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
        distances = {'d12': -0.049406, 'd13': -0.173976, 'd23': -0.128339},
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
        distances = {'d12': 0.070669, 'd13': 0.038898, 'd23': -0.029339},
        uncertainties = {'d12': 0.051853, 'd13': 0.039147, 'd23': 0.043927},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 87 distances.
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=348 label="C_rad/COCs2">]
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
[<Entry index=12 label="ROOH_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
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
        distances = {'d12': 0.070669, 'd13': 0.038898, 'd23': -0.029339},
        uncertainties = {'d12': 0.051853, 'd13': 0.039147, 'd23': 0.043927},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 87 distances.
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=348 label="C_rad/COCs2">]
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
[<Entry index=12 label="ROOH_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
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
        distances = {'d12': 0.070669, 'd13': 0.038898, 'd23': -0.029339},
        uncertainties = {'d12': 0.051853, 'd13': 0.039147, 'd23': 0.043927},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 87 distances.
[<Entry index=38 label="Cd/H/Cd">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=66 label="C/H3/Cs\H2\Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=106 label="C/H2/Cd\H_Cd\H2/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=9 label="O/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=94 label="C/H2/CsO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=47 label="CO/H/OneDe">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=459 label="Cd/H2/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=72 label="C/H3/O">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=31 label="Cd/H/NonDeC">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=4 label="H2">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=152 label="C/H/Cs2CO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=75 label="C/H3/Ct">, <Entry index=348 label="C_rad/COCs2">]
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
[<Entry index=12 label="ROOH_pri">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=45 label="CO/H/Cs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=10 label="O/H/NonDeO">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=105 label="C/H2/CdCs">, <Entry index=348 label="C_rad/COCs2">]
[<Entry index=64 label="C/H3/Cs\H3">, <Entry index=348 label="C_rad/COCs2">]
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
        distances = {'d12': 0.27066, 'd13': 0.154191, 'd23': -0.119354},
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
        distances = {'d12': 0.27066, 'd13': 0.154191, 'd23': -0.119354},
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
        distances = {'d12': 0.27066, 'd13': 0.154191, 'd23': -0.119354},
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
)

entry(
    index = 434,
    label = "N3_rad",
    group = 
"""
1 *3 [N3s,N3d] u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 435,
    label = "N3s_rad",
    group = 
"""
1 *3 N3s u1
""",
    distances = DistanceData(distances={}),
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
)

entry(
    index = 440,
    label = "N5_rad",
    group = 
"""
1 *3 [N5s,N5d,N5t] u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 441,
    label = "N5d_rad",
    group = 
"""
1 *3 N5d u1
""",
    distances = DistanceData(distances={}),
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

