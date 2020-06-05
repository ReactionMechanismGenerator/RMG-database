#!/usr/bin/env python3

###############################################################################
#                                                                             #
# RMG - Reaction Mechanism Generator                                          #
#                                                                             #
# Copyright (c) 2002-2020 Prof. William H. Green (whgreen@mit.edu),           #
# Prof. Richard H. West (r.west@neu.edu) and the RMG Team (rmg_dev@mit.edu)   #
#                                                                             #
# Permission is hereby granted, free of charge, to any person obtaining a     #
# copy of this software and associated documentation files (the 'Software'),  #
# to deal in the Software without restriction, including without limitation   #
# the rights to use, copy, modify, merge, publish, distribute, sublicense,    #
# and/or sell copies of the Software, and to permit persons to whom the       #
# Software is furnished to do so, subject to the following conditions:        #
#                                                                             #
# The above copyright notice and this permission notice shall be included in  #
# all copies or substantial portions of the Software.                         #
#                                                                             #
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER         #
# DEALINGS IN THE SOFTWARE.                                                   #
#                                                                             #
###############################################################################

"""
This file provides atomic energy and BAC parameters for several model
chemistries.
"""

# Atom energy corrections to reach gas-phase reference state
# Experimental enthalpy of formation at 0 K, 1 bar for gas phase
# Data from the Active Thermochemical Tables (version 1.122g)
# Care should be taken that these values are compatible with the BAC values (if BACs are used)
# He, Ne, K, Ca, Ti, Cu, Zn, Ge, Br, Kr, Rb, Ag, Cd, Sn, I, Xe, Cs, Hg, and Pb are taken from CODATA
# Codata: Cox, J. D., Wagman, D. D., and Medvedev, V. A., CODATA Key Values for Thermodynamics, Hemisphere
# Publishing Corp., New York, 1989. (http://www.science.uwaterloo.ca/~cchieh/cact/tools/thermodata.html)

atom_hf = {'H': 51.6334, 'He': -1.481,
           'Li': 37.69, 'Be': 76.48, 'B': 136.2, 'C': 170.028, 'N': 112.471, 'O': 58.9971, 'F': 18.464, 'Ne': -1.481,
           'Na': 25.69, 'Mg': 34.87, 'Al': 78.23, 'Si': 106.6, 'P': 75.42, 'S': 65.66, 'Cl': 28.5901,
           'K': 36.841, 'Ca': 41.014, 'Ti': 111.2, 'Cu': 79.16, 'Zn': 29.685, 'Ge': 87.1, 'Br': 28.1821,
           'Kr': -1.481,
           'Rb': 17.86, 'Ag': 66.61, 'Cd': 25.240, 'Sn': 70.50, 'I': 25.6111, 'Xe': -1.481,
           'Cs': 16.80, 'Hg': 13.19, 'Pb': 15.17}

# Thermal contribution to enthalpy for the atoms reported by Gaussian thermo whitepaper
# This will be subtracted from the corresponding value in atom_hf to produce an enthalpy used in calculating
# the enthalpy of formation at 298 K
atom_thermal = {'H': 1.012, 'He': 1.481,
                'Li': 1.1, 'Be': 0.46, 'B': 0.29, 'C': 0.2512, 'N': 1.036, 'O': 1.037, 'F': 1.055, 'Ne': 1.481,
                'Na': 1.54, 'Mg': 1.19, 'Al': 1.08, 'Si': 0.76, 'P': 1.28, 'S': 1.054, 'Cl': 1.097,
                'K': 1.481, 'Ca': 1.481, 'Ti': 1.802, 'Cu': 1.481, 'Zn': 1.481, 'Ge': 1.768, 'Br': 2.930,
                'Kr': 1.481,
                'Rb': 1.481, 'Ag': 1.481, 'Cd': 1.481, 'Sn': 1.485, 'I': 1.577, 'Xe': 1.481,
                'Cs': 1.481, 'Hg': 1.481, 'Pb': 1.481}

# Spin orbit correction (SOC) in Hartrees
# Values taken from ref 22 of http://dx.doi.org/10.1063/1.477794 and converted to Hartrees
# Values in milli-Hartree are also available (with fewer significant figures) from table VII of
# http://dx.doi.org/10.1063/1.473182
# Iodine SOC calculated as a weighted average of the electronic spin splittings of the lowest energy state.
# The splittings are obtained from Huber, K.P.; Herzberg, G., Molecular Spectra and Molecular Structure. IV.
# Constants of Diatomic Molecules, Van Nostrand Reinhold Co., 1979
# Spin orbit correction for F, Si, Cl, Br and B taken form https://cccbdb.nist.gov/elecspin.asp
SOC = {'H': 0.0, 'N': 0.0, 'O': -0.000355, 'C': -0.000135, 'S': -0.000893, 'P': 0.0, 'I': -0.011547226,
       'F': -0.000614, 'Si': -0.000682, 'Cl': -0.001338, 'Br': -0.005597, 'B': -0.000046}

# Atomic energies
atom_energies = {

    "LevelOfTheory(method='dlpnoccsd(t)',basis='def2tzvp',auxiliary_basis='def2tzvp/c',software='orca',args=('normalpno',))": {
        'H': -0.495120313966199,
        'C': -37.778093385262565,
        'N': -54.50593880634087,
        'O': -74.97031066806414,
        'F': -99.62122592786801,
        'S': -397.63892486619716,
        'Cl': -459.65754747581127,
        'Br': -2572.6616119496057
    },

    "LevelOfTheory(method='dlpnoccsd(t)f12',basis='ccpvdzf12',auxiliary_basis='augccpvdz/c',cabs='ccpvdzf12cabs',software='orca',args=('normalpno',))": {
        'H': -0.499271332870507,
        'C': -37.78035847712249,
        'N': -54.51658215786608,
        'O': -74.98507401946902,
        'F': -99.6400162523877,
        'S': -397.65365372589673,
        'Cl': -459.67474665853644
    },
    "LevelOfTheory(method='dlpnoccsd(t)f12',basis='ccpvdzf12',auxiliary_basis='augccpvdz/c',cabs='ccpvdzf12cabs',software='orca',args=('tightpno',))": {
        'H': -0.4992954866849927,
        'C': -37.78051571097156,
        'N': -54.51730376585899,
        'O': -74.98569618373061,
        'F': -99.6403937442908,
        'S': -397.6543929284361,
        'Cl': -459.67859358474846
    },
    "LevelOfTheory(method='dlpnoccsd(t)f12',basis='ccpvtzf12',auxiliary_basis='augccpvtz/c',cabs='ccpvtzf12cabs',software='orca',args=('normalpno',))": {
        'H': -0.500033623708364,
        'C': -37.78438841108071,
        'N': -54.523924288269974,
        'O': -74.99756159439208,
        'F': -99.65896394490674,
        'S': -397.66715992966283,
        'Cl': -459.6937861504422
    },
    "LevelOfTheory(method='dlpnoccsd(t)f12',basis='ccpvtzf12',auxiliary_basis='augccpvtz/c',cabs='ccpvtzf12cabs',software='orca',args=('tightpno',))": {
        'H': -0.5000040360065064,
        'C': -37.78475070198012,
        'N': -54.524530329963675,
        'O': -74.99813676030882,
        'F': -99.65901604019733,
        'S': -397.66794827125074,
        'Cl': -459.69651783412957
    },

    "LevelOfTheory(method='b3lypd3bj',basis='def2tzvp',software='gaussian')": {
        'H': -0.5010929786112164,
        'C': -37.86564131254798,
        'N': -54.60589708581987,
        'O': -75.09767460743954,
        'F': -99.7683619387686,
        'S': -398.1345106984206,
        'Cl': -460.16503888886285,
        'Br': -2574.1443474092116
    },

    "LevelOfTheory(method='wb97xd',basis='def2tzvp',software='gaussian')": {
        'H': -0.5006557872395984,
        'C': -37.8470621030192,
        'N': -54.58499594718283,
        'O': -75.0725240612682,
        'F': -99.73955550924293,
        'S': -398.11055304016924,
        'Cl': -460.1467876783654,
        'Br': -2574.1745335954856
    },

    "LevelOfTheory(method='wb97mv',basis='def2tzvp',software='qchem')": {
        'H': -0.4927360492667605,
        'C': -37.8496721908121,
        'N': -54.59325884742653,
        'O': -75.07650052379734,
        'F': -99.7408472067375,
        'S': -398.0812825325984,
        'Cl': -460.1106984630151,
        'Br': -2573.9706200243604
    },
    "LevelOfTheory(method='wb97mv',basis='def2tzvpd',software='qchem')": {
        'H': -0.49338216995809725,
        'C': -37.84772407774059,
        'N': -54.59351384873174,
        'O': -75.0774947462408,
        'F': -99.74200231175924,
        'S': -398.0820818202818,
        'Cl': -460.1117669506163,
        'Br': -2573.9713149056824
    },

    # cbs-qb3 and cbs-qb3-paraskevas have the same corrections
    "LevelOfTheory(method='cbsqb3',software='gaussian')": {
        'H': -0.499818 + SOC['H'], 'N': -54.520543 + SOC['N'], 'O': -74.987624 + SOC['O'],
        'C': -37.785385 + SOC['C'], 'P': -340.817186 + SOC['P'], 'S': -397.657360 + SOC['S']
    },
    "LevelOfTheory(method='cbsqb3paraskevas',software='gaussian')": {
        'H': -0.499818 + SOC['H'], 'N': -54.520543 + SOC['N'], 'O': -74.987624 + SOC['O'],
        'C': -37.785385 + SOC['C'], 'P': -340.817186 + SOC['P'], 'S': -397.657360 + SOC['S']
    },

    "LevelOfTheory(method='m062x',basis='ccpvtz',software='gaussian')": {
        'H': -0.498135 + SOC['H'], 'N': -54.586780 + SOC['N'], 'O': -75.064242 + SOC['O'],
        'C': -37.842468 + SOC['C'], 'P': -341.246985 + SOC['P'], 'S': -398.101240 + SOC['S']
    },

    "LevelOfTheory(method='g3',software='gaussian')": {
        'H': -0.5010030, 'N': -54.564343, 'O': -75.030991, 'C': -37.827717, 'P': -341.116432, 'S': -397.961110
    },

    # * indicates that the grid size used in the [QChem] electronic
    # structure calculation utilized 75 radial points and 434 angular points
    # (i.e,, this is specified in the $rem section of the [qchem] input file as: XC_GRID 000075000434)
    "LevelOfTheory(method='m08so',basis='mg3s*',software='qchem')": {
        'H': -0.5017321350 + SOC['H'], 'N': -54.5574039365 + SOC['N'],
        'O': -75.0382931348 + SOC['O'], 'C': -37.8245648740 + SOC['C'],
        'P': -341.2444299005 + SOC['P'], 'S': -398.0940312227 + SOC['S']
    },

    "LevelOfTheory(method='klip_1')": {
        'H': -0.50003976 + SOC['H'], 'N': -54.53383153 + SOC['N'], 'O': -75.00935474 + SOC['O'],
        'C': -37.79266591 + SOC['C']
    },

    # Klip QCI(tz,qz)
    "LevelOfTheory(method='klip_2')": {
        'H': -0.50003976 + SOC['H'], 'N': -54.53169400 + SOC['N'], 'O': -75.00714902 + SOC['O'],
        'C': -37.79060419 + SOC['C']
    },

    # Klip QCI(dz,tz)
    "LevelOfTheory(method='klip_3')": {
        'H': -0.50005578 + SOC['H'], 'N': -54.53128140 + SOC['N'], 'O': -75.00356581 + SOC['O'],
        'C': -37.79025175 + SOC['C']
    },

    # Klip CCSD(T)(tz,qz)
    "LevelOfTheory(method='klip_2_cc')": {
        'H': -0.50003976 + SOC['H'], 'O': -75.00681155 + SOC['O'], 'C': -37.79029443 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvdzf12_htz',software='molpro')": {
        'H': -0.499946213243 + SOC['H'], 'N': -54.526406291655 + SOC['N'],
        'O': -74.995458316117 + SOC['O'], 'C': -37.788203485235 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvdzf12_hqz',software='molpro')": {
        'H': -0.499994558325 + SOC['H'], 'N': -54.526406291655 + SOC['N'],
        'O': -74.995458316117 + SOC['O'], 'C': -37.788203485235 + SOC['C']
    },

    # We are assuming that SOC is included in the Bond Energy Corrections
    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvdzf12',software='molpro')": {
        'H': -0.499811124128, 'N': -54.526406291655, 'O': -74.995458316117,
        'C': -37.788203485235, 'S': -397.663040369707
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvtzf12',software='molpro')": {
        'H': -0.499946213243, 'N': -54.53000909621, 'O': -75.004127673424,
        'C': -37.789862146471, 'S': -397.675447487865
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvqzf12',software='molpro')": {
        'H': -0.499994558325, 'N': -54.530515226371, 'O': -75.005600062003,
        'C': -37.789961656228, 'S': -397.676719774973
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpcvdzf12',software='molpro')": {
        'H': -0.499811124128 + SOC['H'], 'N': -54.582137180344 + SOC['N'],
        'O': -75.053045547421 + SOC['O'], 'C': -37.840869118707 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpcvtzf12',software='molpro')": {
        'H': -0.499946213243 + SOC['H'], 'N': -54.588545831900 + SOC['N'],
        'O': -75.065995072347 + SOC['O'], 'C': -37.844662139972 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpcvqzf12',software='molpro')": {
        'H': -0.499994558325 + SOC['H'], 'N': -54.589137594139 + SOC['N'],
        'O': -75.067412234737 + SOC['O'], 'C': -37.844893820561 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvtzf12(pp)',software='molpro')": {
        'H': -0.499946213243 + SOC['H'], 'N': -54.53000909621 + SOC['N'],
        'O': -75.004127673424 + SOC['O'], 'C': -37.789862146471 + SOC['C'],
        'S': -397.675447487865 + SOC['S'], 'I': -294.81781766 + SOC['I']
    },

    # ccsd(t)/aug-cc-pvtz(-pp) atomic energies were fit to a set of 8 small molecules:
    # CH4, CH3OH, H2S, H2O, SO2, HI, I2, CH3I
    "LevelOfTheory(method='ccsd(t)',basis='augccpvtz(pp)')": {
        'H': -0.499821176024 + SOC['H'], 'O': -74.96738492 + SOC['O'],
        'C': -37.77385697 + SOC['C'], 'S': -397.6461604 + SOC['S'],
        'I': -294.7958443 + SOC['I']
    },

    # note that all atom corrections but S are fitted, the correction for S is calculated
    "LevelOfTheory(method='ccsd(t)f12',basis='augccpvdz',software='molpro')": {
        'H': -0.499459066131 + SOC['H'], 'N': -54.524279516472 + SOC['N'],
        'O': -74.992097308083 + SOC['O'], 'C': -37.786694171716 + SOC['C'],
        'S': -397.648733842400 + SOC['S']
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='augccpvtz',software='molpro')": {
        'H': -0.499844820798 + SOC['H'], 'N': -54.527419359906 + SOC['N'],
        'O': -75.000001429806 + SOC['O'], 'C': -37.788504810868 + SOC['C'],
        'S': -397.666903000231 + SOC['S']
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='augccpvqz',software='molpro')": {
        'H': -0.499949526073 + SOC['H'], 'N': -54.529569719016 + SOC['N'],
        'O': -75.004026586610 + SOC['O'], 'C': -37.789387892348 + SOC['C'],
        'S': -397.671214204994 + SOC['S']
    },

    "LevelOfTheory(method='ccsd(t)f12b',basis='ccpvdzf12',software='molpro')": {
        'H': -0.499811124128 + SOC['H'], 'N': -54.523269942190 + SOC['N'],
        'O': -74.990725918500 + SOC['O'], 'C': -37.785409916465 + SOC['C'],
        'S': -397.658155086033 + SOC['S']
    },

    "LevelOfTheory(method='ccsd(t)f12b',basis='ccpvtzf12',software='molpro')": {
        'H': -0.499946213243 + SOC['H'], 'N': -54.528135889213 + SOC['N'],
        'O': -75.001094055506 + SOC['O'], 'C': -37.788233578503 + SOC['C'],
        'S': -397.671745425929 + SOC['S']
    },

    "LevelOfTheory(method='ccsd(t)f12b',basis='ccpvqzf12',software='molpro')": {
        'H': -0.499994558325 + SOC['H'], 'N': -54.529425753163 + SOC['N'],
        'O': -75.003820485005 + SOC['O'], 'C': -37.789006506290 + SOC['C'],
        'S': -397.674145126931 + SOC['S']
    },

    "LevelOfTheory(method='ccsd(t)f12b',basis='ccpcvdzf12',software='molpro')": {
        'H': -0.499811124128 + SOC['H'], 'N': -54.578602780288 + SOC['N'],
        'O': -75.048064317367 + SOC['O'], 'C': -37.837592033417 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12b',basis='ccpcvtzf12',software='molpro')": {
        'H': -0.499946213243 + SOC['H'], 'N': -54.586402551258 + SOC['N'],
        'O': -75.062767632757 + SOC['O'], 'C': -37.842729156944 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12b',basis='ccpcvqzf12',software='molpro')": {
        'H': -0.49999456 + SOC['H'], 'N': -54.587781507581 + SOC['N'],
        'O': -75.065397706471 + SOC['O'], 'C': -37.843634971592 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12b',basis='augccpvdz',software='molpro')": {
        'H': -0.499459066131 + SOC['H'], 'N': -54.520475581942 + SOC['N'],
        'O': -74.986992215049 + SOC['O'], 'C': -37.783294495799 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12b',basis='augccpvtz',software='molpro')": {
        'H': -0.499844820798 + SOC['H'], 'N': -54.524927371700 + SOC['N'],
        'O': -74.996328829705 + SOC['O'], 'C': -37.786320700792 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12b',basis='augccpvqz',software='molpro')": {
        'H': -0.499949526073 + SOC['H'], 'N': -54.528189769291 + SOC['N'],
        'O': -75.001879610563 + SOC['O'], 'C': -37.788165047059 + SOC['C']
    },

    "LevelOfTheory(method='mp2',basis='ccpvdz')": {
        'H': -0.49927840 + SOC['H'], 'N': -54.46141996 + SOC['N'], 'O': -74.89408254 + SOC['O'],
        'C': -37.73792713 + SOC['C']
    },

    "LevelOfTheory(method='mp2',basis='ccpvtz')": {
        'H': -0.49980981 + SOC['H'], 'N': -54.49615972 + SOC['N'], 'O': -74.95506980 + SOC['O'],
        'C': -37.75833104 + SOC['C']
    },

    "LevelOfTheory(method='mp2',basis='ccpvqz')": {
        'H': -0.49994557 + SOC['H'], 'N': -54.50715868 + SOC['N'], 'O': -74.97515364 + SOC['O'],
        'C': -37.76533215 + SOC['C']
    },

    "LevelOfTheory(method='ccsdf12',basis='ccpvdzf12',software='molpro')": {
        'H': -0.499811124128 + SOC['H'], 'N': -54.524325513811 + SOC['N'],
        'O': -74.992326577897 + SOC['O'], 'C': -37.786213495943 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvdzf12_noscale',software='molpro')": {
        'H': -0.499811124128 + SOC['H'], 'N': -54.526026290887 + SOC['N'],
        'O': -74.994751897699 + SOC['O'], 'C': -37.787881871511 + SOC['C']
    },

    "LevelOfTheory(method='pbepbe',basis='6311++g(d,p)',software='gaussian')": {
        'H': -0.499812273282 + SOC['H'], 'N': -54.5289567564 + SOC['N'],
        'O': -75.0033596764 + SOC['O'], 'C': -37.7937388736 + SOC['C']
    },

    "LevelOfTheory(method='fci',basis='ccpvdz')": {
        'C': -37.789527 + SOC['C']
    },

    "LevelOfTheory(method='fci',basis='ccpvtz')": {
        'C': -37.781266669684 + SOC['C']
    },

    "LevelOfTheory(method='fci',basis='ccpvqz')": {
        'C': -37.787052110598 + SOC['C']
    },

    # 'bmk/cbsb7' and 'bmk/6-311g(2d,d,p)' have the same corrections
    "LevelOfTheory(method='bmk',basis='cbsb7',software='gaussian')": {
        'H': -0.498618853119 + SOC['H'], 'N': -54.5697851544 + SOC['N'],
        'O': -75.0515210278 + SOC['O'], 'C': -37.8287310027 + SOC['C'],
        'P': -341.167615941 + SOC['P'], 'S': -398.001619915 + SOC['S']
    },
    "LevelOfTheory(method='bmk',basis='6311g(2d,d,p)',software='gaussian')": {
        'H': -0.498618853119 + SOC['H'], 'N': -54.5697851544 + SOC['N'],
        'O': -75.0515210278 + SOC['O'], 'C': -37.8287310027 + SOC['C'],
        'P': -341.167615941 + SOC['P'], 'S': -398.001619915 + SOC['S']
    },

    # Fitted to small molecules
    "LevelOfTheory(method='b3lyp',basis='631g(d,p)',software='gaussian')": {
        'H': -0.500426155, 'C': -37.850331697831, 'O': -75.0535872748806, 'S': -398.100820107242
    },

    # Calculated atomic energies
    "LevelOfTheory(method='b3lyp',basis='6311+g(3df,2p)',software='gaussian')": {
        'H': -0.502155915123 + SOC['H'], 'C': -37.8574709934 + SOC['C'],
        'N': -54.6007233609 + SOC['N'], 'O': -75.0909131284 + SOC['O'],
        'P': -341.281730319 + SOC['P'], 'S': -398.134489850 + SOC['S']
    },

    "LevelOfTheory(method='wb97xd',basis='augccpvtz',software='gaussian')": {
        'H': -0.502803 + SOC['H'], 'N': -54.585652 + SOC['N'], 'O': -75.068286 + SOC['O'],
        'C': -37.842014 + SOC['C']
    },

    # Calculated atomic energies (unfitted)
    "LevelOfTheory(method='mrci+davidson',basis='augccpv(t+d)z',software='molpro')": {
        'H': -0.49982118 + SOC['H'], 'C': -37.78321274 + SOC['C'], 'N': -54.51729444 + SOC['N'],
        'O': -74.97847534 + SOC['O'], 'S': -397.6571654 + SOC['S']
    },

}

# Petersson-type bond additivity correction parameters
pbac = {

    "CompositeLevelOfTheory(freq=LevelOfTheory(method='wb97xd',basis='def2svp',software='gaussian'),energy=LevelOfTheory(method='dlpnoccsd(t)',basis='def2tzvp',auxiliary_basis='def2tzvp/c',software='orca',args=('normalpno',)))": {
        'Br-Br': -0.2870880330716341,
        'Br-C': -0.4478244666388548,
        'Br-Cl': 0.01837965082522075,
        'Br-H': 1.6780662633351326,
        'Br-O': -1.301571848215788,
        'C#C': -5.633874730579925,
        'C#N': -2.350388264540849,
        'C#O': -2.335340001589028,
        'C-C': -2.0453036348643705,
        'C-Cl': -0.7937283757778072,
        'C-H': 0.060425951533927366,
        'C-N': -1.651911129849335,
        'C-O': -1.796575976909021,
        'C-S': -2.0064816208335787,
        'C=C': -4.027654792752827,
        'C=N': -2.468988776355673,
        'C=O': -2.7113274393461415,
        'C=S': -3.4249096030317427,
        'Cl-Cl': 0.23762115749830404,
        'Cl-H': 0.9576358955354785,
        'Cl-N': -0.5462426893162307,
        'Cl-O': -0.5947482611382665,
        'Cl-S': -1.9524146070719532,
        'H-H': 2.1991874131397684,
        'H-N': -0.10477615687090823,
        'H-O': -0.4804520793569034,
        'H-S': 0.8890697618555344,
        'N#N': 1.7172710606758559,
        'N-N': -0.23525051157489782,
        'N-O': -2.3357975143561958,
        'N=N': -0.3724056990519406,
        'N=O': -1.012867200400173,
        'O-O': -1.9265283393618704,
        'O-S': -3.290481766296215,
        'O=O': -6.1544835261552135,
        'O=S': -3.712702079003568,
        'S-S': -2.4197555320429056,
        'S=S': -4.631694904246286
    },

    "LevelOfTheory(method='wb97mv',basis='def2tzvp',software='qchem')": {
        'Br-Br': 0.12883478274287885,
        'Br-C': -0.150030250962165,
        'Br-Cl': 0.12285796401693849,
        'Br-H': 0.6540969617674097,
        'Br-O': -1.1582528732790545,
        'C#C': -4.748712039948744,
        'C#N': -2.0665880339508202,
        'C#O': -2.057520673483758,
        'C-C': -0.6725999001509286,
        'C-Cl': -0.06527363707880929,
        'C-H': 0.05562827091211855,
        'C-N': 0.4440243026501112,
        'C-O': -0.27952034032707135,
        'C-S': -0.4037485090125749,
        'C=C': -2.050572602612211,
        'C=N': -0.7651823847170863,
        'C=O': -0.9589155446625549,
        'C=S': -1.7560291368147039,
        'Cl-Cl': 0.37369510583772764,
        'Cl-H': -0.12256884341346819,
        'Cl-N': 0.8993489069647221,
        'Cl-O': -0.06451520407346098,
        'Cl-S': 0.21961266720279804,
        'H-H': 0.3322563608529926,
        'H-N': 0.5384834163563573,
        'H-O': -0.30250996255851864,
        'H-S': 1.2990380895838174,
        'N#N': 0.6398826224795257,
        'N-N': 2.2893826067208063,
        'N-O': 1.1647309212826926,
        'N=N': 1.158973366276253,
        'N=O': -2.003462090716991,
        'O-O': -0.36083119662182433,
        'O-S': -1.0586430830495528,
        'O=O': -9.787297094731814,
        'O=S': -2.0867984872066594,
        'S-S': 0.11403843016877874,
        'S=S': -4.248907677734486
    },

    "CompositeLevelOfTheory(freq=LevelOfTheory(method='wb97mv',basis='def2tzvpd',software='qchem'),energy=LevelOfTheory(method='dlpnoccsd(t)f12',basis='ccpvtzf12',auxiliary_basis='augccpvtz/c',cabs='ccpvtzf12cabs',software='orca',args=('normalpno',)))": {
        'C#C': -0.9952393577480061,
        'C#N': -0.21670408478225422,
        'C#O': 0.08584143921783394,
        'C-C': -0.06383852159915943,
        'C-Cl': 0.1811303534132533,
        'C-F': 0.4689290057963229,
        'C-H': -0.05769272935605165,
        'C-N': 0.11187111971803186,
        'C-O': -0.1950053472722554,
        'C-S': -0.22423573364290136,
        'C=C': -0.434739278594919,
        'C=N': -0.6069121063625295,
        'C=O': -0.5819720516967676,
        'C=S': -1.6777875548451746,
        'Cl-Cl': 0.2602805433930088,
        'Cl-F': 1.1977077936265417,
        'Cl-H': 0.14080025124600937,
        'Cl-N': -0.03565133829176556,
        'Cl-O': -0.31876250793438815,
        'Cl-S': -0.08250391784877557,
        'F-F': -0.7052874467288989,
        'F-H': 0.5088069611601611,
        'F-O': -1.1715289986733404,
        'F-S': 0.8409641852483484,
        'H-H': -0.5090509328796105,
        'H-N': -0.1830816795252867,
        'H-O': 0.056316828775832536,
        'H-S': 0.5259974694588669,
        'N#N': 0.29959908061441387,
        'N-N': 0.8300450116878976,
        'N-O': -0.37333841475485446,
        'N=N': 0.28369958177637694,
        'N=O': -2.14757940107408,
        'O-O': -1.6076480204170003,
        'O-S': -0.6840233114920843,
        'O=O': -5.056631239388305,
        'O=S': 0.031913927897726,
        'S-S': -0.5254496256224851,
        'S=S': -2.7452116139981637
    },

    "CompositeLevelOfTheory(freq=LevelOfTheory(method='wb97mv',basis='def2tzvpd',software='qchem'),energy=LevelOfTheory(method='dlpnoccsd(t)f12',basis='ccpvdzf12',auxiliary_basis='augccpvdz/c',cabs='ccpvdzf12cabs',software='orca',args=('normalpno',)))": {
        'C#C': -1.8809858243575,
        'C#N': -0.8815633180197873,
        'C#O': -0.6289055371994579,
        'C-C': -0.6313184180355716,
        'C-Cl': 0.20506551750787366,
        'C-F': -0.08442970874883365,
        'C-H': -0.06879513047270383,
        'C-N': -0.5586789938167999,
        'C-O': -1.0204079798619372,
        'C-S': -0.34294495991280005,
        'C=C': -1.1840521668409254,
        'C=N': -1.1503663619494995,
        'C=O': -1.6126462042362875,
        'C=S': -1.8150097366144733,
        'Cl-Cl': 0.25067042064305295,
        'Cl-F': 0.9343985981312972,
        'Cl-H': 0.2745155200047158,
        'Cl-N': -0.07166700318347963,
        'Cl-O': -0.5118116587256177,
        'Cl-S': 0.422147961624741,
        'F-F': -0.6912144548070561,
        'F-H': 0.42743853854365454,
        'F-O': -1.7056068509234503,
        'F-S': 0.7659902001989186,
        'H-H': 0.0202473635657149,
        'H-N': -0.2744958158744846,
        'H-O': -0.1639175312572552,
        'H-S': 0.645720684834329,
        'N#N': 0.8055842721640124,
        'N-N': 0.1799746493068582,
        'N-O': -1.3820408316063708,
        'N=N': -0.08473563935713535,
        'N=O': -2.256018202142908,
        'O-O': -2.331592864330181,
        'O-S': -1.026842195765298,
        'O=O': -4.754221564294066,
        'O=S': 0.10775770960222222,
        'S-S': -0.5992483105093566,
        'S=S': -2.2823274317290143
    },

    "LevelOfTheory(method='b3lypd3bj',basis='def2tzvp',software='gaussian')": {
        'Br-Br': 0.5185156767091978,
        'Br-C': -0.9577504278588156,
        'Br-Cl': 0.775822683599642,
        'Br-H': 0.4572616416556361,
        'Br-O': 0.2043742691865884,
        'C#C': -5.38720460824316,
        'C#N': -1.4697566930299064,
        'C#O': -8.37401091882317,
        'C-C': -2.7695071290444933,
        'C-Cl': -0.9774345169996838,
        'C-H': 0.05806248235595328,
        'C-N': -0.7840938182617309,
        'C-O': -2.2116962927406383,
        'C-S': -2.4737081990029157,
        'C=C': -2.443173148719635,
        'C=N': -0.8239045314834288,
        'C=O': -2.2192234101953763,
        'C=S': -2.0285045935931953,
        'Cl-Cl': 1.0785419856630345,
        'Cl-H': 0.04915737799971254,
        'Cl-N': 3.7499799567518544,
        'Cl-O': 0.763405809596614,
        'Cl-S': 0.27732415760384654,
        'H-H': 1.909833906261407,
        'H-N': 0.976608941059378,
        'H-O': -1.567801028736581,
        'H-S': 0.5700725801878385,
        'N#N': -1.9800094030561088,
        'N-N': 3.2062861973173673,
        'N-O': 1.3853348209888028,
        'N=N': 3.7974680237792295,
        'N=O': -0.33242521937722463,
        'O-O': 0.3248931710140498,
        'O-S': -3.2896810976569797,
        'O=O': -8.92878449794968,
        'O=S': -4.456237634540539,
        'S-S': -0.5198234606383603,
        'S=S': -3.7746270990364343
    },

    "CompositeLevelOfTheory(freq=LevelOfTheory(method='wb97mv',basis='def2tzvpd',software='qchem'),energy=LevelOfTheory(method='dlpnoccsd(t)f12',basis='ccpvdzf12',auxiliary_basis='augccpvdz/c',cabs='ccpvdzf12cabs',software='orca',args=('tightpno',)))": {
        'C#C': -1.756875490417629,
        'C#N': -0.7910748130090758,
        'C#O': -0.3561622578251047,
        'C-C': -0.532777968807306,
        'C-Cl': 0.3839557624854567,
        'C-F': 0.06047319228098636,
        'C-H': -0.08913044484855878,
        'C-N': -0.4925240800863085,
        'C-O': -0.910834642190212,
        'C-S': 0.03792163671788884,
        'C=C': -1.0436942758183232,
        'C=N': -1.144498230892254,
        'C=O': -1.290098834270545,
        'C=S': -0.8152840616847224,
        'Cl-Cl': 0.1305534856935172,
        'Cl-F': 0.6000247256961817,
        'Cl-H': 0.48616831967622787,
        'Cl-N': -0.04998410524204344,
        'Cl-O': -0.4229320348083118,
        'Cl-S': 1.09797306578115,
        'F-F': -0.7495565788415806,
        'F-H': 0.5277056723384845,
        'F-O': -1.3253990742158896,
        'F-S': 0.6675443759031244,
        'H-H': -0.010066131029286067,
        'H-N': -0.38410161078823923,
        'H-O': -0.24242289671270353,
        'H-S': 1.0398027744830538,
        'N#N': 0.8345805799170924,
        'N-N': 0.31355605986304547,
        'N-O': -1.194149176390521,
        'N=N': -0.045645561818263396,
        'N=O': -2.01290308953839,
        'O-O': -2.13543778284453,
        'O-S': -0.8420123742257197,
        'O=O': -4.428877728186617,
        'O=S': 0.10454618546073133,
        'S-S': 0.2680328516552689,
        'S=S': -1.0258630305973666
    },

    "CompositeLevelOfTheory(freq=LevelOfTheory(method='wb97mv',basis='def2tzvpd',software='qchem'),energy=LevelOfTheory(method='dlpnoccsd(t)f12',basis='ccpvtzf12',auxiliary_basis='augccpvtz/c',cabs='ccpvtzf12cabs',software='orca',args=('tightpno',)))": {
        'C#C': -1.0417389384809002,
        'C#N': -0.18997811213150434,
        'C#O': 0.11597961664107714,
        'C-C': -0.0874428175410642,
        'C-Cl': 0.35756758240886416,
        'C-F': 0.6205829581209822,
        'C-H': -0.07483538208032497,
        'C-N': 0.10483919847165243,
        'C-O': -0.22297787183511178,
        'C-S': 0.1404832465782864,
        'C=C': -0.45913593181331386,
        'C=N': -0.6215972359059202,
        'C=O': -0.6263159879358061,
        'C=S': -0.8114169321909457,
        'Cl-Cl': 0.09583452431516075,
        'Cl-F': 0.3664507611788004,
        'Cl-H': 0.37287630516855685,
        'Cl-N': 0.14385756310153153,
        'Cl-O': -0.44981597674284113,
        'Cl-S': 0.38460170657528187,
        'F-F': -0.4981836231875576,
        'F-H': 0.11758523789195863,
        'F-O': -1.0986502231981488,
        'F-S': 0.9647209073295073,
        'H-H': -0.47236174775511974,
        'H-N': -0.22649067211716103,
        'H-O': -0.07562933770900222,
        'H-S': 0.9073212171759294,
        'N#N': 0.40151149779116896,
        'N-N': 0.850874207833184,
        'N-O': -0.42947725200427334,
        'N=N': 0.37600825315112596,
        'N=O': -1.9562351875057598,
        'O-O': -1.500224679745408,
        'O-S': -0.6174870980141091,
        'O=O': -4.494140521331516,
        'O=S': -0.17591534884630283,
        'S-S': 0.20052268818794297,
        'S=S': -1.8902601269101473
    },

    "CompositeLevelOfTheory(freq=LevelOfTheory(method='wb97xd',basis='def2tzvp',software='gaussian'),energy=LevelOfTheory(method='dlpnoccsd(t)',basis='def2tzvp',auxiliary_basis='def2tzvp/c',software='orca',args=('normalpno',)))": {
        'Br-Br': -0.3547689067627191,
        'Br-C': -0.4543904814746382,
        'Br-Cl': -0.07302627413413987,
        'Br-H': 1.6975460370847149,
        'Br-O': -1.471102822838629,
        'C#C': -5.831729359702083,
        'C#N': -2.51406808426462,
        'C#O': -2.4114089646190457,
        'C-C': -2.0760003450257245,
        'C-Cl': -0.7893313438167636,
        'C-H': 0.053567940484746474,
        'C-N': -1.6157150573369121,
        'C-O': -1.7139336189171057,
        'C-S': -2.059268815084767,
        'C=C': -4.09124969861493,
        'C=N': -2.4906100662038826,
        'C=O': -2.683456260373795,
        'C=S': -3.5199473387282176,
        'Cl-Cl': 0.14513940970876957,
        'Cl-H': 0.9949309780326345,
        'Cl-N': -0.5989447726914174,
        'Cl-O': -0.5728849630186141,
        'Cl-S': -1.7110599110994906,
        'H-H': 2.2420633723751804,
        'H-N': -0.12763553876237166,
        'H-O': -0.46993285948595703,
        'H-S': 0.9155385392761627,
        'N#N': 1.472143327988522,
        'N-N': -0.11387528606939841,
        'N-O': -2.1250551224160255,
        'N=N': -0.4474833988114753,
        'N=O': -1.0714043137383475,
        'O-O': -1.7136048475662717,
        'O-S': -3.123924956844675,
        'O=O': -5.963363797942465,
        'O=S': -3.752895679048051,
        'S-S': -2.466234634483199,
        'S=S': -4.907887651788898
    },

    "LevelOfTheory(method='wb97xd',basis='def2tzvp',software='gaussian')": {
        'Br-Br': 0.016045619067636352,
        'Br-C': -1.0401173711203133,
        'Br-Cl': 0.2983927031966531,
        'Br-H': 0.9415811759953474,
        'Br-O': -1.5611232414179237,
        'C#C': -7.22638483094488,
        'C#N': -3.025697788832491,
        'C#O': -7.031708654318713,
        'C-C': -1.2939356753685136,
        'C-Cl': -0.9496033384719503,
        'C-H': 0.18748207622260252,
        'C-N': 0.33806423908535604,
        'C-O': -1.4847965500532676,
        'C-S': -1.680227500725586,
        'C=C': -3.2447299874715707,
        'C=N': -0.935406901068859,
        'C=O': -2.3043966309101966,
        'C=S': -3.4749183307650258,
        'Cl-Cl': 0.39648213676177524,
        'Cl-H': 0.10677101518796661,
        'Cl-N': 0.953874070689174,
        'Cl-O': -1.3793439739818782,
        'Cl-S': -0.5348211607370006,
        'H-H': 0.22480639824807758,
        'H-N': 1.038629931847478,
        'H-O': -1.0042110205565615,
        'H-S': 0.9630019170637759,
        'N#N': -0.780153706091782,
        'N-N': 3.62665588475469,
        'N-O': 0.7831718131424773,
        'N=N': 2.6853663579609024,
        'N=O': -0.849094503813265,
        'O-O': -1.5235846478681454,
        'O-S': -3.2453957184035045,
        'O=O': -9.953519761276839,
        'O=S': -3.4945349305218114,
        'S-S': -1.3155402429488239,
        'S=S': -5.848810185696702
    },

    "LevelOfTheory(method='wb97mv',basis='def2tzvpd',software='qchem')": {
        'Br-Br': 0.1958610046250353,
        'Br-C': 0.08342615830647254,
        'Br-Cl': 0.15262164580006665,
        'Br-F': 1.554766957397149,
        'Br-H': 0.5081557501289318,
        'Br-O': -1.2236043316175111,
        'C#C': -2.6349164523184414,
        'C#N': -1.1906643794269727,
        'C#O': -1.2169066048908732,
        'C-C': -0.05280224931801543,
        'C-Cl': 0.09412550983382971,
        'C-F': 1.657136384442864,
        'C-H': -0.01586761480957165,
        'C-N': 0.8464785445254364,
        'C-O': -0.022295634798634844,
        'C-S': -0.1201537369814494,
        'C=C': -0.8020718163585956,
        'C=N': -0.23249839836435446,
        'C=O': -0.6923581569910078,
        'C=S': -1.4039224541066722,
        'Cl-Cl': 0.24706245542077263,
        'Cl-F': 1.5870013888348105,
        'Cl-H': -0.061538610443722774,
        'Cl-N': 0.9215949633998766,
        'Cl-O': -0.10690598725501184,
        'Cl-S': -0.26928317951073,
        'F-F': 0.7076947926501269,
        'F-H': -0.7608076549745562,
        'F-O': 0.6414896651183406,
        'F-S': 1.0255233686038518,
        'H-H': -0.4548842455328711,
        'H-N': 0.32770189779757325,
        'H-O': -0.3482010477866195,
        'H-S': 1.0420963399199659,
        'N#N': 0.446870060585342,
        'N-N': 2.4305267415020237,
        'N-O': 1.0847843547592344,
        'N=N': 1.2304781903332842,
        'N=O': -2.379892376833476,
        'O-O': -0.8522025877305646,
        'O-S': -1.3007885702567272,
        'O=O': -9.628885866255034,
        'O=S': -2.1776302846961637,
        'S-S': 0.14292519243155768,
        'S=S': -3.3100912737119246
    },

    # 'S-H', 'C-S', 'C=S', 'S-S', 'O-S', 'O=S', 'O=S=O' taken from http://hdl.handle.net/1721.1/98155 (both for
    # 'CCSD(T)-F12/cc-pVDZ-F12' and 'CCSD(T)-F12/cc-pVTZ-F12')
    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvdzf12',software='molpro')": {
        'C-H': -0.46, 'C-C': -0.68, 'C=C': -1.90, 'C#C': -3.13,
        'O-H': -0.51, 'C-O': -0.23, 'C=O': -0.69, 'O-O': -0.02, 'C-N': -0.67,
        'C=N': -1.46, 'C#N': -2.79, 'N-O': 0.74, 'N_O': -0.23, 'N=O': -0.51,
        'N-H': -0.69, 'N-N': -0.47, 'N=N': -1.54, 'N#N': -2.05, 'S-H': 0.87,
        'C-S': 0.42, 'C=S': 0.51, 'S-S': 0.86, 'O-S': 0.23, 'O=S': -0.53,
        'O=S=O': 1.95
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvtzf12',software='molpro')": {
        'C-H': -0.09, 'C-C': -0.27, 'C=C': -1.03, 'C#C': -1.79,
        'O-H': -0.06, 'C-O': 0.14, 'C=O': -0.19, 'O-O': 0.16, 'C-N': -0.18,
        'C=N': -0.41, 'C#N': -1.41, 'N-O': 0.87, 'N_O': -0.09, 'N=O': -0.23,
        'N-H': -0.01, 'N-N': -0.21, 'N=N': -0.44, 'N#N': -0.76, 'S-H': 0.52,
        'C-S': 0.13, 'C=S': -0.12, 'S-S': 0.30, 'O-S': 0.15, 'O=S': -2.61,
        'O=S=O': 0.27
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvqzf12',software='molpro')": {
        'C-H': -0.08, 'C-C': -0.26, 'C=C': -1.01, 'C#C': -1.66,
        'O-H': 0.07, 'C-O': 0.25, 'C=O': -0.03, 'O-O': 0.26, 'C-N': -0.20,
        'C=N': -0.30, 'C#N': -1.33, 'N-O': 1.01, 'N_O': -0.03, 'N=O': -0.26,
        'N-H': 0.06, 'N-N': -0.23, 'N=N': -0.37, 'N#N': -0.64
    },

    "LevelOfTheory(method='cbsqb3',software='gaussian')": {
        'C-H': -0.11, 'C-C': -0.30, 'C=C': -0.08, 'C#C': -0.64, 'O-H': 0.02, 'C-O': 0.33, 'C=O': 0.55,
        # Table IX: Petersson GA (1998) J. of Chemical Physics, DOI: 10.1063/1.477794
        'N-H': -0.42, 'C-N': -0.13, 'C#N': -0.89, 'C-F': 0.55, 'C-Cl': 1.29, 'S-H': 0.0, 'C-S': 0.43,
        'O=S': -0.78,
        'N=O': 1.11, 'N-N': -1.87, 'N=N': -1.58, 'N-O': 0.35,
        # Table 2: Ashcraft R (2007) J. Phys. Chem. B; DOI: 10.1021/jp073539t
        'N#N': -2.0, 'O=O': -0.2, 'H-H': 1.1,  # Unknown source
    },

    "LevelOfTheory(method='cbsqb3paraskevas',software='gaussian')": {
        # NOTE: The Paraskevas corrections are inaccurate for non-oxygenated hydrocarbons,
        # and may do poorly in combination with the Petersson corrections
        'C-C': -0.495, 'C-H': -0.045, 'C=C': -0.825, 'C-O': 0.378, 'C=O': 0.743, 'O-H': -0.423,
        # Table2: Paraskevas, PD (2013). Chemistry-A European J., DOI: 10.1002/chem.201301381
        'C#C': -0.64, 'C#N': -0.89, 'C-S': 0.43, 'O=S': -0.78, 'S-H': 0.0, 'C-N': -0.13, 'C-Cl': 1.29,
        'C-F': 0.55,  # Table IX: Petersson GA (1998) J. of Chemical Physics, DOI: 10.1063/1.477794
        'N-H': -0.42, 'N=O': 1.11, 'N-N': -1.87, 'N=N': -1.58, 'N-O': 0.35,
        # Table 2: Ashcraft R (2007) J. Phys. Chem. B; DOI: 10.1021/jp073539t
        'N#N': -2.0, 'O=O': -0.2, 'H-H': 1.1,  # Unknown source
    },

    # Identical corrections for 'b3lyp/cbsb7', 'b3lyp/6-311g(2d,d,p)', 'b3lyp/6-311+g(3df,2p)', 'b3lyp/6-31g(d,p)'
    "LevelOfTheory(method='b3lyp',basis='cbsb7',software='gaussian')": {
        'C-H': 0.25, 'C-C': -1.89, 'C=C': -0.40, 'C#C': -1.50,
        'O-H': -1.09, 'C-O': -1.18, 'C=O': -0.01, 'N-H': 1.36, 'C-N': -0.44,
        'C#N': 0.22, 'C-S': -2.35, 'O=S': -5.19, 'S-H': -0.52,
    },
    "LevelOfTheory(method='b3lyp',basis='6311g(2d,d,p)',software='gaussian')": {
        'C-H': 0.25, 'C-C': -1.89, 'C=C': -0.40, 'C#C': -1.50,
        'O-H': -1.09, 'C-O': -1.18, 'C=O': -0.01, 'N-H': 1.36, 'C-N': -0.44,
        'C#N': 0.22, 'C-S': -2.35, 'O=S': -5.19, 'S-H': -0.52,
    },
    "LevelOfTheory(method='b3lyp',basis='6311+g(3df,2p)',software='gaussian')": {
        'C-H': 0.25, 'C-C': -1.89, 'C=C': -0.40, 'C#C': -1.50,
        'O-H': -1.09, 'C-O': -1.18, 'C=O': -0.01, 'N-H': 1.36, 'C-N': -0.44,
        'C#N': 0.22, 'C-S': -2.35, 'O=S': -5.19, 'S-H': -0.52,
    },
    "LevelOfTheory(method='b3lyp',basis='631g(d,p)',software='gaussian')": {
        'C-H': 0.25, 'C-C': -1.89, 'C=C': -0.40, 'C#C': -1.50,
        'O-H': -1.09, 'C-O': -1.18, 'C=O': -0.01, 'N-H': 1.36, 'C-N': -0.44,
        'C#N': 0.22, 'C-S': -2.35, 'O=S': -5.19, 'S-H': -0.52,
    },

}

# Melius-type bond additivity correction parameters
mbac = {

    "CompositeLevelOfTheory(freq=LevelOfTheory(method='wb97xd',basis='def2svp',software='gaussian'),energy=LevelOfTheory(method='dlpnoccsd(t)',basis='def2tzvp',auxiliary_basis='def2tzvp/c',software='orca',args=('normalpno',)))": {
        'atom_corr': {
            'Br': -1.150753507340495,
            'C': -0.8040011721434682,
            'Cl': -0.7786714015490848,
            'H': -0.1610651059581168,
            'N': -1.8658882153945768,
            'O': 0.3538423919890405,
            'S': -2.9020771837491823
        },
        'bond_corr_length': {
            'Br': 1961.0976436215374,
            'C': 202.27005569815617,
            'Cl': 228.4560331625716,
            'H': 0.36610444730409564,
            'N': 53.182965731803016,
            'O': 24.595847582555724,
            'S': 2230.286563373731
        },
        'bond_corr_neighbor': {
            'Br': -0.22693593653362212,
            'C': 0.011181659018191582,
            'Cl': 0.14404875714141083,
            'H': -0.12731233800275885,
            'N': 0.1825908685494787,
            'O': 0.12616949153596407,
            'S': 0.1161616289037561
        },
        'mol_corr': -0.4487396083184329
    },

    "LevelOfTheory(method='wb97mv',basis='def2tzvp',software='qchem')": {
        'atom_corr': {
            'Br': -1.2994941498489196,
            'C': 1.485589630298389,
            'Cl': -0.885497073736691,
            'H': -1.277975959905759,
            'N': -1.3381571569260102,
            'O': -1.4810010154090956,
            'S': -0.9448929015832052
        },
        'bond_corr_length': {
            'Br': 1840.421180262182,
            'C': 3.364621581449355,
            'Cl': 93.3859593172456,
            'H': 3.227837776164252,
            'N': 17.346752846534777,
            'O': 150.1005669526723,
            'S': 329.8957846521883
        },
        'bond_corr_neighbor': {
            'Br': 0.14354691695386906,
            'C': -0.04852442504083006,
            'Cl': -0.007011907639231679,
            'H': 0.09120540077765624,
            'N': -0.19375527951006943,
            'O': -0.04698250213294315,
            'S': -0.09827674794826893
        },
        'mol_corr': -0.8364492191467792
    },

    "CompositeLevelOfTheory(freq=LevelOfTheory(method='wb97mv',basis='def2tzvpd',software='qchem'),energy=LevelOfTheory(method='dlpnoccsd(t)f12',basis='ccpvtzf12',auxiliary_basis='augccpvtz/c',cabs='ccpvtzf12cabs',software='orca',args=('normalpno',)))": {
        'atom_corr': {
            'C': -1.416920566293708,
            'Cl': -0.4200559299675974,
            'F': -0.2993477558592458,
            'H': -0.600459687190157,
            'N': -0.7476120199894484,
            'O': 0.6801789919340411,
            'S': -0.9373017954157762
        },
        'bond_corr_length': {
            'C': 77.50625137536059,
            'Cl': 63.531108990774214,
            'F': 7.612715257261074e-17,
            'H': 1.176870012661965,
            'N': 6.953591468748732,
            'O': 1.177890858065914e-17,
            'S': 700.8342186840581
        },
        'bond_corr_neighbor': {
            'C': -0.0356621803391651,
            'Cl': -0.046233300650657234,
            'F': -0.026152571967311487,
            'H': 0.12578893100791433,
            'N': -0.002803669157031435,
            'O': -0.05988253241309233,
            'S': -0.1349775614811328
        },
        'mol_corr': -0.5762389263082766
    },

    "CompositeLevelOfTheory(freq=LevelOfTheory(method='wb97mv',basis='def2tzvpd',software='qchem'),energy=LevelOfTheory(method='dlpnoccsd(t)f12',basis='ccpvdzf12',auxiliary_basis='augccpvdz/c',cabs='ccpvdzf12cabs',software='orca',args=('normalpno',)))": {
        'atom_corr': {
            'C': -0.13618588897638187,
            'Cl': -1.0202909242030385,
            'F': -1.310938248692034,
            'H': -0.8863475219299282,
            'N': -1.802329701164756,
            'O': -0.5939237246646104,
            'S': -0.21597431861839964
        },
        'bond_corr_length': {
            'C': 1.1236131324991416,
            'Cl': 9.250484012840152,
            'F': 130.9730937067238,
            'H': 0.34412298658240625,
            'N': 10.580584596772654,
            'O': 97.32054526429285,
            'S': 8.963262765640016e-37
        },
        'bond_corr_neighbor': {
            'C': 0.0010750106772896397,
            'Cl': -0.043617241563568034,
            'F': 0.10313508761471367,
            'H': 0.003313809586782813,
            'N': 0.07321134185228698,
            'O': 0.034284973076121925,
            'S': -0.1596291616167065
        },
        'mol_corr': -1.2892400629268028
    },

    "LevelOfTheory(method='b3lypd3bj',basis='def2tzvp',software='gaussian')": {
        'atom_corr': {
            'Br': -2.871729911568782,
            'C': -1.3419167625995925,
            'Cl': -2.9651214556544656,
            'H': -3.114980999128395,
            'N': -4.924326298384489,
            'O': -4.999999999999999,
            'S': -3.3925874022291898
        },
        'bond_corr_length': {
            'Br': 2631.9637073123527,
            'C': 63.738365607463365,
            'Cl': 581.2291799334001,
            'H': 19.208130319016973,
            'N': 23.89697799951957,
            'O': 260.0614872024786,
            'S': 792.781184185199
        },
        'bond_corr_neighbor': {
            'Br': 0.22065107274594775,
            'C': 0.09705844364422887,
            'Cl': 0.3473967982906402,
            'H': 0.0061635645102511944,
            'N': -0.10776324055195008,
            'O': 0.1445617604626904,
            'S': 0.11500345710920869
        },
        'mol_corr': -2.5980867963328214
    },

    "CompositeLevelOfTheory(freq=LevelOfTheory(method='wb97mv',basis='def2tzvpd',software='qchem'),energy=LevelOfTheory(method='dlpnoccsd(t)f12',basis='ccpvdzf12',auxiliary_basis='augccpvdz/c',cabs='ccpvdzf12cabs',software='orca',args=('tightpno',)))": {
        'atom_corr': {
            'C': -1.1303244112178317,
            'Cl': -0.6916868408502033,
            'F': -0.5472566236302432,
            'H': -0.5668743519282876,
            'N': -1.2943080692710867,
            'O': 0.3414764655701705,
            'S': -2.039105925103035
        },
        'bond_corr_length': {
            'C': 63.448757861684975,
            'Cl': 3.4201559481603134e-21,
            'F': 1.4492621129066053e-25,
            'H': 0.032837915485316886,
            'N': 6.455481215190162,
            'O': 5.098389438242963e-29,
            'S': 703.5308421980434
        },
        'bond_corr_neighbor': {
            'C': -0.013449553939336986,
            'Cl': -0.06782548501870386,
            'F': 0.05931201643106704,
            'H': 0.06513467634802346,
            'N': 0.05192633216797187,
            'O': 0.036407584364074555,
            'S': -0.1735290682409047
        },
        'mol_corr': -1.034988562496322
    },

    "CompositeLevelOfTheory(freq=LevelOfTheory(method='wb97mv',basis='def2tzvpd',software='qchem'),energy=LevelOfTheory(method='dlpnoccsd(t)f12',basis='ccpvtzf12',auxiliary_basis='augccpvtz/c',cabs='ccpvtzf12cabs',software='orca',args=('tightpno',)))": {
        'atom_corr': {
            'C': -0.3821870761810326,
            'Cl': -0.5635119135371978,
            'F': -1.2161685479466757,
            'H': -0.5486956411113301,
            'N': -1.3844264459694926,
            'O': -0.42173634712354335,
            'S': -0.5977405924400462
        },
        'bond_corr_length': {
            'C': 2.5499355433408896e-20,
            'Cl': 7.167682714394459,
            'F': 115.84884251044593,
            'H': 0.020872501855810188,
            'N': 7.80750691722819,
            'O': 80.83435781994227,
            'S': 10.317954375843414
        },
        'bond_corr_neighbor': {
            'C': -0.01831237685033945,
            'Cl': -0.12201701986677872,
            'F': 0.02667428939998246,
            'H': 0.03065782957509031,
            'N': 0.004004157940874455,
            'O': -0.037794888079462276,
            'S': -0.13845488076414272
        },
        'mol_corr': -0.9282505817816508
    },

    "CompositeLevelOfTheory(freq=LevelOfTheory(method='wb97xd',basis='def2tzvp',software='gaussian'),energy=LevelOfTheory(method='dlpnoccsd(t)',basis='def2tzvp',auxiliary_basis='def2tzvp/c',software='orca',args=('normalpno',)))": {
        'atom_corr': {
            'Br': -1.1208142416454387,
            'C': -0.759761984637026,
            'Cl': -0.7439329234009516,
            'H': -0.1328201787596902,
            'N': -1.7703648929488864,
            'O': 0.2718273230223588,
            'S': -2.680641023581836
        },
        'bond_corr_length': {
            'Br': 2006.080088146316,
            'C': 200.59527224856626,
            'Cl': 192.1573909145208,
            'H': 0.11433624891972258,
            'N': 50.416479624122466,
            'O': 24.554651180154544,
            'S': 2002.4888301520427
        },
        'bond_corr_neighbor': {
            'Br': -0.24521615999188243,
            'C': 0.0096556232345116,
            'Cl': 0.14278739102392546,
            'H': -0.09382231088482801,
            'N': 0.16647480979372034,
            'O': 0.11044912260118399,
            'S': 0.10757092771071239
        },
        'mol_corr': -0.4710263534748382
    },

    "LevelOfTheory(method='wb97xd',basis='def2tzvp',software='gaussian')": {
        'atom_corr': {
            'Br': -3.500404614452807,
            'C': 0.6043384108781988,
            'Cl': -2.2199867323856046,
            'H': -2.697298969939275,
            'N': -4.813583567105453,
            'O': -3.705141560518769,
            'S': -2.0470365288143086
        },
        'bond_corr_length': {
            'Br': 3855.3219992167105,
            'C': 5.265929765122098,
            'Cl': 395.15445737554194,
            'H': 7.004552459950368,
            'N': 5.842909193095168,
            'O': 193.62341632004774,
            'S': 346.55692844813734
        },
        'bond_corr_neighbor': {
            'Br': 0.7022794185349223,
            'C': -0.0675116935249027,
            'Cl': 0.2542743481491643,
            'H': 0.049067908864623394,
            'N': -0.24464250898424794,
            'O': 0.15899890845973066,
            'S': -0.02495699084856554
        },
        'mol_corr': -3.045051588951062
    },

    "LevelOfTheory(method='wb97mv',basis='def2tzvpd',software='qchem')": {
        'atom_corr': {
            'Br': -1.2684797610740068,
            'C': -0.4174257352393245,
            'Cl': -0.9661365064678925,
            'F': -2.7269618018691286,
            'H': -0.8200512641588867,
            'N': -1.9268795831605057,
            'O': -1.2065799989531332,
            'S': -1.4981603387204314
        },
        'bond_corr_length': {
            'Br': 1080.374675861722,
            'C': 0.9866591151048302,
            'Cl': 14.168290439224558,
            'F': 53.677336144261815,
            'H': 0.10560986920930937,
            'N': 7.102031391504367,
            'O': 116.712690311844,
            'S': 282.9043317540571
        },
        'bond_corr_neighbor': {
            'Br': 0.0646368151807638,
            'C': -0.04831303352995286,
            'Cl': 0.014147411281693778,
            'F': 0.05343762573411219,
            'H': 0.011152914014086364,
            'N': -0.23350242741116362,
            'O': -0.10294376619330678,
            'S': -0.07865422498372374
        },
        'mol_corr': -1.4470179217148968
    },

}


# Frequency scale factors
#    Refer to https://comp.chem.umn.edu/freqscale/index.html for future updates of these factors
#
#    Sources:
#        [1] I.M. Alecu, J. Zheng, Y. Zhao, D.G. Truhlar, J. Chem. Theory Comput. 2010, 6, 2872, DOI: 10.1021/ct100326h
#        [2] http://cccbdb.nist.gov/vibscalejust.asp
#        [3] http://comp.chem.umn.edu/freqscale/190107_Database_of_Freq_Scale_Factors_v4.pdf
#        [4] Calculated as described in 10.1021/ct100326h
#        [5] J.A. Montgomery, M.J. Frisch, J. Chem. Phys. 1999, 110, 2822–2827, DOI: 10.1063/1.477924

freq_dict = {"LevelOfTheory(method='hf',basis='sto3g')": 0.817,  # [2]
             "LevelOfTheory(method='hf',basis='631g')": 0.903,  # [2]
             "LevelOfTheory(method='hf',basis='631g(d)')": 0.899,  # [2]
             "LevelOfTheory(method='hf',basis='631g(d,p)')": 0.903,  # [2]
             "LevelOfTheory(method='hf',basis='631g+(d,p)')": 0.904,  # [2]
             "LevelOfTheory(method='hf',basis='631+g(d,p)')": 0.915 * 1.014,  # [1] Table 7
             "LevelOfTheory(method='pm3')": 0.940 * 1.014,  # [1] Table 7, the 0.940 value is the ZPE scale factor
             "LevelOfTheory(method='pm6')": 1.078 * 1.014,  # [1] Table 7, the 1.078 value is the ZPE scale factor
             "LevelOfTheory(method='b3lyp',basis='631g(d,p)')": 0.961,  # [2]
             "LevelOfTheory(method='b3lyp',basis='6311g(d,p)')": 0.967,  # [2]
             "LevelOfTheory(method='b3lyp',basis='6311+g(3df,2p)')": 0.967,  # [2]
             "LevelOfTheory(method='b3lyp',basis='6311+g(3df,2pd)')": 0.970,  # [2]
             "LevelOfTheory(method='b3lyp-d3bj',basis='def2-tzvp')": 0.999,  # [4]
             "LevelOfTheory(method='m062x',basis='631g(d,p)')": 0.952,  # [2]
             "LevelOfTheory(method='m062x',basis='631+g(d,p)')": 0.979,  # [3]
             "LevelOfTheory(method='m062x',basis='6311+g(d,p)')": 0.983,  # [3]
             "LevelOfTheory(method='m062x',basis='6311++g(d,p)')": 0.983,  # [3]
             "LevelOfTheory(method='m062x',basis='ccpvtz')": 0.955,  # [2]
             "LevelOfTheory(method='m062x',basis='augccpvdz')": 0.993,  # [3]
             "LevelOfTheory(method='m062x',basis='augccpvtz')": 0.985,  # [1] Table 3, [3]
             "LevelOfTheory(method='m062x',basis='def2tzvp')": 0.984,  # [3]
             "LevelOfTheory(method='m062x',basis='def2qzvp')": 0.983,  # [3]
             "LevelOfTheory(method='m062x',basis='def2tzvpp')": 0.983,  # [1] Table 3, [3]
             "LevelOfTheory(method='m08so',basis='mg3s*')": 0.995,  # [1] Table 3, taken as 'M08-SO/MG3S'
             "LevelOfTheory(method='wb97xd',basis='augccpvtz',software='gaussian')": 0.988,  # [3], taken as 'ωB97X-D/maug-cc-pVTZ'
             "LevelOfTheory(method='wb97xd',basis='6311++g(d,p)',software='gaussian')": 0.988,  # [4]
             "LevelOfTheory(method='wb97xd',basis='def2tzvp',software='gaussian')": 0.988,  # [4]
             "LevelOfTheory(method='wb97xd',basis='def2svp',software='gaussian')": 0.986,  # [4]
             "LevelOfTheory(method='wb97mv',basis='def2tzvp')": 1.001,  # [4]
             "LevelOfTheory(method='wb97mv',basis='def2tzvpd')": 1.002,  # [4]
             "LevelOfTheory(method='apfd',basis='def2tzvp')": 0.993,  # [4]
             "LevelOfTheory(method='apfd',basis='def2tzvpp')": 0.992,  # [4]
             "LevelOfTheory(method='mp2',basis='ccpvdz')": 0.953,  # [2]
             "LevelOfTheory(method='mp2',basis='ccpvtz')": 0.950,  # [2]
             "LevelOfTheory(method='mp2',basis='ccpvqz')": 0.962,  # [2]
             "LevelOfTheory(method='cbsqb3')": 0.99 * 1.014,  # [5], the 0.99 value is the ZPE scale factor of CBS-QB3
             "LevelOfTheory(method='cbsqb3paraskevas')": 0.99 * 1.014,  # [5], the 0.99 value is the ZPE scale factor of CBS-QB3
             "LevelOfTheory(method='ccsdf12',basis='ccpvdzf12')": 0.947,  # [2], taken as 'CCSD/cc-pVDZ'
             "LevelOfTheory(method='ccsd(t)',basis='ccpvdz')": 0.979,  # [2]
             "LevelOfTheory(method='ccsd(t)',basis='ccpvtz')": 0.975,  # [2]
             "LevelOfTheory(method='ccsd(t)',basis='ccpvqz')": 0.970,  # [2]
             "LevelOfTheory(method='ccsd(t)',basis='augccpvdz')": 0.963,  # [2]
             "LevelOfTheory(method='ccsd(t)',basis='augccpvtz')": 1.001,  # [3]
             "LevelOfTheory(method='ccsd(t)',basis='augccpvqz')": 0.975,  # [2]
             "LevelOfTheory(method='ccsd(t)',basis='ccpv(t+d)z')": 0.965,  # [2]
             "LevelOfTheory(method='ccsd(t)f12',basis='ccpvdzf12')": 0.997,  # [3], taken as 'CCSD(T)-F12a/cc-pVDZ-F12'
             "LevelOfTheory(method='ccsd(t)f12',basis='ccpvtzf12')": 0.998,  # [3], taken as 'CCSD(T)-F12a/cc-pVTZ-F12'
             "LevelOfTheory(method='ccsd(t)f12',basis='ccpvqzf12',)": 0.998,  # [3], taken as 'CCSD(T)-F12b/VQZF12//CCSD(T)-F12a/TZF'
             "LevelOfTheory(method='ccsd(t)f12',basis='ccpcvdzf12')": 0.997,  # [3], taken as 'CCSD(T)-F12a/cc-pVDZ-F12'
             "LevelOfTheory(method='ccsd(t)f12',basis='ccpcvtzf12')": 0.998,  # [3], taken as 'CCSD(T)-F12a/cc-pVTZ-F12'
             "LevelOfTheory(method='ccsd(t)f12',basis='augccpvdz')": 0.997,  # [3], taken as 'CCSD(T)/cc-pVDZ'
             "LevelOfTheory(method='ccsd(t)f12',basis='augccpvtz')": 0.998,  # [3], taken as CCSD(T)-F12a/cc-pVTZ-F12
             "LevelOfTheory(method='ccsd(t)f12',basis='augccpvqz')": 0.998,  # [3], taken as 'CCSD(T)-F12b/VQZF12//CCSD(T)-F12a/TZF'
             }
