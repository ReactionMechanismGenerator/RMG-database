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
# See Gaussian thermo whitepaper at http://gaussian.com/thermo/
# Note: These values are relatively old and some improvement may be possible by using newer values
# (particularly for carbon).
# However, care should be taken to ensure that they are compatible with the BAC values (if BACs are used)
# He, Ne, K, Ca, Ti, Cu, Zn, Ge, Br, Kr, Rb, Ag, Cd, Sn, I, Xe, Cs, Hg, and Pb are taken from CODATA
# Codata: Cox, J. D., Wagman, D. D., and Medvedev, V. A., CODATA Key Values for Thermodynamics, Hemisphere
# Publishing Corp., New York, 1989. (http://www.science.uwaterloo.ca/~cchieh/cact/tools/thermodata.html)

atom_hf = {'H': 51.63, 'He': -1.481,
           'Li': 37.69, 'Be': 76.48, 'B': 136.2, 'C': 169.98, 'N': 112.53, 'O': 58.99, 'F': 18.47, 'Ne': -1.481,
           'Na': 25.69, 'Mg': 34.87, 'Al': 78.23, 'Si': 106.6, 'P': 75.42, 'S': 65.66, 'Cl': 28.59,
           'K': 36.841, 'Ca': 41.014, 'Ti': 111.2, 'Cu': 79.16, 'Zn': 29.685, 'Ge': 87.1, 'Br': 25.26,
           'Kr': -1.481,
           'Rb': 17.86, 'Ag': 66.61, 'Cd': 25.240, 'Sn': 70.50, 'I': 24.04, 'Xe': -1.481,
           'Cs': 16.80, 'Hg': 13.19, 'Pb': 15.17}

# Thermal contribution to enthalpy for the atoms reported by Gaussian thermo whitepaper
# This will be subtracted from the corresponding value in atom_hf to produce an enthalpy used in calculating
# the enthalpy of formation at 298 K
atom_thermal = {'H': 1.01, 'He': 1.481,
                'Li': 1.1, 'Be': 0.46, 'B': 0.29, 'C': 0.25, 'N': 1.04, 'O': 1.04, 'F': 1.05, 'Ne': 1.481,
                'Na': 1.54, 'Mg': 1.19, 'Al': 1.08, 'Si': 0.76, 'P': 1.28, 'S': 1.05, 'Cl': 1.1,
                'K': 1.481, 'Ca': 1.481, 'Ti': 1.802, 'Cu': 1.481, 'Zn': 1.481, 'Ge': 1.768, 'Br': 1.481,
                'Kr': 1.481,
                'Rb': 1.481, 'Ag': 1.481, 'Cd': 1.481, 'Sn': 1.485, 'I': 1.481, 'Xe': 1.481,
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


    "LevelOfTheory(method='wb97xd3',basis='def2tzvp',software='qchem')": {
        'H': -0.49991749801833063,
        'C': -37.84993993601866,
        'N': -54.58750889521559,
        'O': -75.07402423801669,
        'F': -99.7392410428872,
        'S': -398.10051734579775,
        'Cl': -460.1341841971797,
        'Br': -2574.175384284091
    },

    "LevelOfTheory(method='b97d3',basis='def2msvp',software='qchem')": {
        'H': -0.49516021903680546,
        'C': -37.833878658169624,
        'N': -54.541699219144505,
        'O': -75.01524900146931,
        'F': -99.65948092488345,
        'S': -397.97912317555034,
        'Cl': -459.9963616463421,
        'Br': -2575.1192984500663
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
    # cbs-qb3-rmg is calculated based on the workflow of the AEJob. In gaussian, cbs-qb3(sp)
    # is used to avoid optimization and freq calculation.
    "LevelOfTheory(method='cbsqb3rmg',software='gaussian')": {
        'H': -0.5003409222835609,
        'C': -37.78372087719202,
        'N': -54.51985323975646,
        'O': -74.98822418407062,
        'F': -99.64381432983413,
        'S': -397.65864503995164,
        'Cl': -459.68495386430743,
        'Br': -2572.829883362477
    },

    "LevelOfTheory(method='m062x',basis='ccpvtz',software='gaussian')": {
        'H': -0.498135 + SOC['H'], 'N': -54.586780 + SOC['N'], 'O': -75.064242 + SOC['O'],
        'C': -37.842468 + SOC['C'], 'P': -341.246985 + SOC['P'], 'S': -398.101240 + SOC['S']
    },

    "LevelOfTheory(method='g3',software='gaussian')": {
        'H': -0.5010030, 'N': -54.564343, 'O': -75.030991, 'C': -37.827717, 'P': -341.116432, 'S': -397.961110
    },

    "LevelOfTheory(method='g4',software='gaussian')": {
        'H': -0.5014687881579407,
        'C': -37.83455302489995,
        'N': -54.57384992023183,
        'O': -75.04536783772085,
        'F': -99.70482475665924,
        'S': -397.979812093602,
        'Cl': -460.0142827624398,
        'Br': -2573.5845451893033
    },

    "LevelOfTheory(method='g4mp2',software='gaussian')": {
        'H': -0.5024570094369775,
        'C': -37.793214295980725,
        'N': -54.5327999874644,
        'O': -75.00161654920923,
        'F': -99.65936651240345,
        'S': -397.67718160509025,
        'Cl': -459.70385673640703,
        'Br': -2572.849823345047
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
	    'H': -0.50000836574607,
	    'C': -37.784271457731904,
	    'N': -54.523156256858144,
	    'O': -74.99320041804718,
	    'F': -99.6511861642652,
	    'S': -397.6625539051389,
	    'Cl': -459.68886861844055
	},

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvtzf12',software='molpro')": {
        'H': -0.5003554055415579,
        'C': -37.787690380768844,
        'N': -54.52874573314225,
        'O': -75.00314974528959,
        'F': -99.6658140570029,
        'S': -397.67549377693314,
        'Cl': -459.70521576925796
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

    "LevelOfTheory(method='g4mp2',software='gaussian')": {
        'Br-Br': 3.1825419329719367,
        'Br-C': 2.255168312600869,
        'Br-Cl': 2.123111934238661,
        'Br-F': 2.1775395715570216,
        'Br-H': 2.043013648526953,
        'Br-O': 1.8659543476053828,
        'C#C': 1.4263995136429206,
        'C#N': 1.017116887862132,
        'C#O': 2.8938905176420278,
        'C-C': 0.25972664816085855,
        'C-Cl': 0.7336404140525018,
        'C-F': 0.22492903760789515,
        'C-H': -0.04560994581165702,
        'C-N': 0.22223503587047233,
        'C-O': 0.27615185562122746,
        'C-S': 0.4996484276182482,
        'C=C': 1.1464726433918542,
        'C=N': 0.24838192033780154,
        'C=O': 1.041536379363234,
        'C=S': 1.1570767234268227,
        'Cl-Cl': 0.4174197861119044,
        'Cl-F': 0.0651640133972542,
        'Cl-H': -0.005221824215958293,
        'Cl-N': 0.26954613134171884,
        'Cl-O': -0.33421248325609015,
        'Cl-S': -0.15168082778269437,
        'F-F': -0.6296851138848945,
        'F-H': 0.38960392689780576,
        'F-O': -0.09180119747142101,
        'F-S': 0.12271465131178161,
        'H-H': 0.5347393274410585,
        'H-N': -0.5753345332866951,
        'H-O': -0.11133378465865026,
        'H-S': 0.5147802871619049,
        'N#N': 0.2023326711383128,
        'N-N': 1.3239012818188969,
        'N-O': 0.27766177505497014,
        'N=N': 0.7874041073574481,
        'N=O': 0.3665677245456587,
        'O-O': -0.009850173782670498,
        'O-S': -0.9632216164679775,
        'O=O': 0.20841243572479973,
        'O=S': -0.16205669093480807,
        'S-S': 0.851096892687231,
        'S=S': 0.3931132887399439
    },

    "LevelOfTheory(method='g4',software='gaussian')": {
        'Br-Br': 3.3309142425855747,
        'Br-C': 2.2083243843294706,
        'Br-Cl': 2.0830890161147617,
        'Br-F': 2.6676138865460626,
        'Br-H': 1.7471079802883427,
        'Br-O': 1.7395435493672728,
        'C#C': -0.19447792484338036,
        'C#N': 0.3748853774010142,
        'C#O': 0.8049052606395151,
        'C-C': -0.1230298757362711,
        'C-Cl': 0.5784340510800081,
        'C-F': -0.021938482720594624,
        'C-H': -0.08896161568586525,
        'C-N': 0.22668923729771878,
        'C-O': 0.11018920747231313,
        'C-S': 0.21235539140284548,
        'C=C': -0.11703029523164052,
        'C=N': -0.3563589811893884,
        'C=O': 0.2780794115126253,
        'C=S': 0.6547920792287026,
        'Cl-Cl': 0.45068086369371474,
        'Cl-F': 0.7163697824588393,
        'Cl-H': 0.0645720673944652,
        'Cl-N': 0.39263159891711874,
        'Cl-O': 0.03239354668626438,
        'Cl-S': 0.1600457665184496,
        'F-F': -0.5678629820959131,
        'F-H': 0.28668050670849254,
        'F-O': -0.03959518476334245,
        'F-S': 0.0888390569355882,
        'H-H': 0.2771105077170708,
        'H-N': -0.42557034054954423,
        'H-O': -0.19919493352177597,
        'H-S': 0.4636383296022682,
        'N#N': 0.25687604100131806,
        'N-N': 1.300928743386193,
        'N-O': 0.6366250135116676,
        'N=N': 0.8599243535135134,
        'N=O': -0.03442630171112671,
        'O-O': -0.2029876953581943,
        'O-S': -0.6862482538866865,
        'O=O': 0.14310796729041,
        'O=S': -0.5261881824748176,
        'S-S': 0.559212964528034,
        'S=S': -0.5531243709922784
    },

    "LevelOfTheory(method='cbsqb3rmg',software='gaussian')": {
        'Br-Br': 2.226040134887289,
        'Br-C': 3.2841867961622486,
        'Br-Cl': 1.5772848602919853,
        'Br-F': 2.0366375748141525,
        'Br-H': 2.290745667205142,
        'Br-O': 2.582451473523784,
        'C#C': 0.7563097309572258,
        'C#N': 1.055111119930898,
        'C#O': 1.1447291205022196,
        'C-C': 0.45984517718233403,
        'C-Cl': 1.096724515771227,
        'C-F': 0.8777552699975305,
        'C-H': -0.15905127913919428,
        'C-N': 0.9877814307013724,
        'C-O': 0.9158746775698626,
        'C-S': 0.4504722966060509,
        'C=C': 0.8086850609904329,
        'C=N': 0.35896639286244464,
        'C=O': 0.8654987688457523,
        'C=S': 0.7224691684154109,
        'Cl-Cl': 0.15853766421954427,
        'Cl-F': -1.0274298208469421,
        'Cl-H': 0.03366479739513295,
        'Cl-N': 0.5281860142962359,
        'Cl-O': -0.307119319676113,
        'Cl-S': -0.2698453056375285,
        'F-F': -0.0753727011143634,
        'F-H': 0.09702167511309767,
        'F-O': -0.2284702904503897,
        'F-S': -0.9257527256897523,
        'H-H': 0.47714421672507906,
        'H-N': -0.5705186716712036,
        'H-O': -0.3781849565797784,
        'H-S': 0.3964680904760937,
        'N#N': 0.2328442415609497,
        'N-N': 2.100081744666711,
        'N-O': 1.285789233241441,
        'N=N': 1.523268137640888,
        'N=O': 0.05564725620448339,
        'O-O': 0.08918724207362907,
        'O-S': -1.0421911539185107,
        'O=O': -1.1751603025557325,
        'O=S': -0.6801160541851019,
        'S-S': 0.42219720539052474,
        'S=S': -1.189727115802033
    },

    "CompositeLevelOfTheory(freq=LevelOfTheory(method='wb97xd3',basis='def2tzvp',software='qchem'),energy=LevelOfTheory(method='ccsd(t)f12',basis='ccpvtzf12',software='molpro'))": {
        'C#C': -0.404744030989917,
        'C#N': -0.08505486104685218,
        'C#O': 0.6409755137896376,
        'C-C': 0.08610003768431868,
        'C-Cl': 0.3824681488129294,
        'C-F': 0.5059900907597003,
        'C-H': -0.06628040972299173,
        'C-N': 0.25894229529649393,
        'C-O': 0.1820834134037927,
        'C-S': 0.03729359183349243,
        'C=C': -0.08483024784920973,
        'C=N': -0.47917805301848726,
        'C=O': 0.024183807634378295,
        'C=S': -0.7949628214405438,
        'Cl-Cl': 0.13012800825824125,
        'Cl-F': 0.3707551128040638,
        'Cl-H': 0.13509532902839894,
        'Cl-N': 0.39332735774385436,
        'Cl-O': 0.276768173044111,
        'Cl-S': 0.2088068612353694,
        'F-F': -0.6624729037388452,
        'F-H': 0.02949171902966441,
        'F-O': -0.5756771022989073,
        'F-S': 0.8288296603082396,
        'H-H': -0.32685290722198723,
        'H-N': -0.3445663790446433,
        'H-O': -0.09099930133179272,
        'H-S': 0.5431357697840049,
        'N#N': 0.12223342110802092,
        'N-N': 1.1887655301582138,
        'N-O': 0.1739540911021752,
        'N=N': 0.41106332195793716,
        'N=O': -1.0667222695706366,
        'O-O': -0.6346542818276062,
        'O-S': -0.4613671639775802,
        'O=O': -2.9265821381997146,
        'O=S': 0.2776508312191951,
        'S-S': 0.09872955772978363,
        'S=S': -1.6147498898801558
    },

    "CompositeLevelOfTheory(freq=LevelOfTheory(method='wb97xd3',basis='def2tzvp',software='qchem'),energy=LevelOfTheory(method='ccsd(t)f12',basis='ccpvdzf12',software='molpro'))": {
        'C#C': -0.8256193462108072,
        'C#N': -0.31471770905274377,
        'C#O': 1.1720730632859997,
        'C-C': -0.04607497525800651,
        'C-Cl': 0.7420009494761749,
        'C-F': 0.44881519534763925,
        'C-H': -0.08627216047799781,
        'C-N': 0.06107461631205359,
        'C-O': 0.06039128813351924,
        'C-S': 0.3872922111682926,
        'C=C': -0.36362250188425316,
        'C=N': -0.7235831377469741,
        'C=O': -0.04713424146278478,
        'C=S': -0.4765543991611835,
        'Cl-Cl': -0.02259378118112597,
        'Cl-F': 0.6339852644486914,
        'Cl-H': 0.3175884647888445,
        'Cl-N': 0.5696202996745275,
        'Cl-O': 0.497044330188489,
        'Cl-S': 0.6375514855194503,
        'F-F': -0.7239522658833698,
        'F-H': 0.05805582733381698,
        'F-O': -0.6024866285929253,
        'F-S': 0.9248172077132987,
        'H-H': -0.09503561001880052,
        'H-N': -0.4961060281626276,
        'H-O': -0.14978895786494278,
        'H-S': 0.829641430928596,
        'N#N': 0.6049567681288514,
        'N-N': 0.9869515491622932,
        'N-O': -0.07127395806231757,
        'N=N': 0.13242149734451855,
        'N=O': -0.8418755827738148,
        'O-O': -0.7560484183200771,
        'O-S': -0.21263665021244277,
        'O=O': -2.7428160179534586,
        'O=S': 0.8907664041090392,
        'S-S': 0.1340301496690316,
        'S=S': -0.9932608633989859
    },

    "LevelOfTheory(method='b97d3',basis='def2msvp',software='qchem')": {
        'Br-Br': 3.315234689218899,
        'Br-C': -0.6501770243317702,
        'Br-Cl': 2.542499978206828,
        'Br-F': 3.929497918011963,
        'Br-H': 3.145068228328528,
        'Br-O': -7.331233264225279,
        'C#C': -19.76271436906988,
        'C#N': -7.50261484079471,
        'C#O': -18.475251655615217,
        'C-C': -6.502474008499422,
        'C-Cl': -1.9295797932548284,
        'C-F': -1.978943824748321,
        'C-H': 0.015272985560806323,
        'C-N': -1.7481717039390876,
        'C-O': -3.8557672175914632,
        'C-S': -5.424907646919267,
        'C=C': -13.002322011253877,
        'C=N': -5.028376340707719,
        'C=O': -6.804268898503189,
        'C=S': -5.660476558309709,
        'Cl-Cl': 1.3419636114215037,
        'Cl-F': 3.4896063856767956,
        'Cl-H': 0.807529583003987,
        'Cl-N': 11.418842571081852,
        'Cl-O': 5.483828939956695,
        'Cl-S': -3.023832905927554,
        'F-F': 5.001729541970344,
        'F-H': -8.586384879573217,
        'F-O': 4.482471816386985,
        'F-S': -4.166540505128751,
        'H-H': 8.526122581696823,
        'H-N': 1.2150232705221626,
        'H-O': -3.858981461845585,
        'H-S': 1.8188149230085722,
        'N#N': 2.7961003581366506,
        'N-N': 5.167876764940302,
        'N-O': 3.554234305355582,
        'N=N': 8.729813431683823,
        'N=O': 5.08904985799338,
        'O-O': 2.561889268475112,
        'O-S': -8.585430074508146,
        'O=O': 1.3106241431687642,
        'O=S': -14.2338893814112,
        'S-S': -4.2642222733737984,
        'S=S': -3.6335953825844403
    },

    "LevelOfTheory(method='wb97xd3',basis='def2tzvp',software='qchem')": {
        'Br-Br': 2.8538858565496312,
        'Br-C': 0.7442401000295052,
        'Br-Cl': 1.4802614230284123,
        'Br-F': 2.736416255234433,
        'Br-H': 2.621870101881271,
        'Br-O': -2.5510160842523026,
        'C#C': -7.91960784624303,
        'C#N': -3.860455324547094,
        'C#O': -7.484045443140786,
        'C-C': -1.0772001044563568,
        'C-Cl': -0.5670310970376374,
        'C-F': 1.3766542915303055,
        'C-H': 0.07938022932013884,
        'C-N': 0.5972252882959622,
        'C-O': -1.259196317662621,
        'C-S': -1.2748522563980267,
        'C=C': -3.8862751982539425,
        'C=N': -1.5033572837368452,
        'C=O': -2.9468957723283116,
        'C=S': -3.706130122985358,
        'Cl-Cl': 0.14035451859517376,
        'Cl-F': 1.0460174011173589,
        'Cl-H': 0.3209071204050744,
        'Cl-N': 1.2589061707705715,
        'Cl-O': -1.1999427296795562,
        'Cl-S': -0.34505860235932717,
        'F-F': 1.2374483962826126,
        'F-H': -1.4703521338319447,
        'F-O': -0.00481009762224401,
        'F-S': 0.31703599826755635,
        'H-H': 0.1674983039100733,
        'H-N': 0.7829258148049894,
        'H-O': -1.2420066240352847,
        'H-S': 1.1920057754210482,
        'N#N': -0.1508747278060373,
        'N-N': 3.441798241932213,
        'N-O': 1.45170459319669,
        'N=N': 2.787293888398078,
        'N=O': -2.386682841759072,
        'O-O': -2.2679171626630166,
        'O-S': -2.648106828015405,
        'O=O': -9.840277224921445,
        'O=S': -3.4653022668813835,
        'S-S': -1.3200354762558415,
        'S=S': -6.862407370669403
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

    "LevelOfTheory(method='g4mp2',software='gaussian')": {
        'atom_corr': {
            'Br': -1.4915844627125625,
            'C': -2.7512277043292026,
            'Cl': 0.5127819966308358,
            'F': 0.262655406951958,
            'H': -0.2342371810751631,
            'N': -1.033248396741043,
            'O': 0.4245201174273713,
            'S': -0.4101930583663664
        },
        'bond_corr_length': {
            'Br': 1.0271869375176743,
            'C': 112.49526602104365,
            'Cl': 8.632003249341508e-25,
            'F': 21.35589787007852,
            'H': 14.224774825758146,
            'N': 104.24933705864605,
            'O': 9.259818329277959,
            'S': 127.42198810535105
        },
        'bond_corr_neighbor': {
            'Br': 0.09370967914171599,
            'C': 0.01034361891811473,
            'Cl': -0.019677651560457515,
            'F': -0.0993723784787344,
            'H': 0.00408620169227999,
            'N': -0.06892957296583548,
            'O': 0.04127835733259136,
            'S': 0.04203975083022801
        },
        'mol_corr': 0.6484063739365641
    },

    "LevelOfTheory(method='g4',software='gaussian')": {
        'atom_corr': {
            'Br': -2.9210673080599334,
            'C': -0.47316368961049976,
            'Cl': -0.3609014942069403,
            'F': 0.0019393139639493626,
            'H': 0.4086058807330258,
            'N': -0.32626829888072795,
            'O': -0.7386617734455345,
            'S': -1.0724624846879784
        },
        'bond_corr_length': {
            'Br': 2472.8750029169896,
            'C': 8.089545496175521,
            'Cl': 79.6145719575692,
            'F': 3.3671570813330867,
            'H': 0.000633568336116583,
            'N': 1.80285167136584,
            'O': 65.64060880263094,
            'S': 265.6031027831911
        },
        'bond_corr_neighbor': {
            'Br': 0.10063663450436904,
            'C': 0.018385442615427083,
            'Cl': -0.13487606027844853,
            'F': -0.04014105341001025,
            'H': -0.12012217720158508,
            'N': -0.02027557195784234,
            'O': -0.03289621712763652,
            'S': -0.011276257081442951
        },
        'mol_corr': -0.1401827506285409
    },

    "LevelOfTheory(method='cbsqb3rmg',software='gaussian')": {
        'atom_corr': {
            'Br': -3.063461560575575,
            'C': -0.3412261735058414,
            'Cl': -0.18195585411830187,
            'F': -0.521630433342473,
            'H': 1.0595558057542571,
            'N': 0.6514416967507799,
            'O': 0.12329748762734198,
            'S': -0.5154949041298995
        },
        'bond_corr_length': {
            'Br': 4125.290425343718,
            'C': 2.4939252573260444,
            'Cl': 718.0044213475622,
            'F': 101.32401422291117,
            'H': 2.0544774514776485e-29,
            'N': 0.7571350346474921,
            'O': 71.56781642678057,
            'S': 380.8655575883884
        },
        'bond_corr_neighbor': {
            'Br': -0.0359264853367919,
            'C': -0.0016224929048357503,
            'Cl': -0.2058143527493474,
            'F': 0.006351394928053059,
            'H': -0.1051388800005577,
            'N': -0.0876979580059308,
            'O': -0.14661735132529424,
            'S': 0.0490030089945193
        },
        'mol_corr': 0.650082722894988
    },

    "CompositeLevelOfTheory(freq=LevelOfTheory(method='wb97xd3',basis='def2tzvp',software='qchem'),energy=LevelOfTheory(method='ccsd(t)f12',basis='ccpvtzf12',software='molpro'))": {
        'atom_corr': {
            'C': -0.6049434931301926,
            'Cl': -0.23077543932816577,
            'F': 0.19821323214490177,
            'H': 0.20747417736624696,
            'N': 0.4202798259871041,
            'O': 0.760116395211634,
            'S': -0.16147845010276898
        },
        'bond_corr_length': {
            'C': 58.062493089340165,
            'Cl': 74.10943324769735,
            'F': 1.4377439015727678e-39,
            'H': 0.03744417328084726,
            'N': 8.061038590242537,
            'O': 6.683467348145323e-30,
            'S': 341.87512901154463
        },
        'bond_corr_neighbor': {
            'C': -0.02485705082889029,
            'Cl': -0.0245325744056343,
            'F': -0.09465388223557501,
            'H': 0.08616740943190652,
            'N': -0.02783616693381088,
            'O': -0.039010302622124314,
            'S': -0.07184889676177111
        },
        'mol_corr': 0.2756910344003536
    },

    "CompositeLevelOfTheory(freq=LevelOfTheory(method='wb97xd3',basis='def2tzvp',software='qchem'),energy=LevelOfTheory(method='ccsd(t)f12',basis='ccpvdzf12',software='molpro'))": {
        'atom_corr': {
            'C': -0.8716131728274684,
            'Cl': -0.4954243144865678,
            'F': 0.17078004042637365,
            'H': -0.6210624216340295,
            'N': -0.5255083858520018,
            'O': 0.21556351519130929,
            'S': 0.3264663336580509
        },
        'bond_corr_length': {
            'C': 45.51002923428158,
            'Cl': 39.37697879681639,
            'F': 7.699774342443738e-37,
            'H': 23.556905315212855,
            'N': 39.39181619115637,
            'O': 9.74390765578037,
            'S': 8.183713902636408e-33
        },
        'bond_corr_neighbor': {
            'C': -0.002889058375866059,
            'Cl': -0.10543058889990209,
            'F': -0.12928382915386433,
            'H': -0.10697009039750834,
            'N': -0.047712632443669196,
            'O': -0.07786330461368522,
            'S': -0.11745625110156013
        },
        'mol_corr': -0.04522805049841732
    },

    "LevelOfTheory(method='b97d3',basis='def2msvp',software='qchem')": {
        'atom_corr': {
            'Br': -4.265361902383324,
            'C': 4.999999999999999,
            'Cl': -4.999999999999999,
            'F': -4.999999999999999,
            'H': -1.0449744344969651,
            'N': -4.999999999999999,
            'O': -4.999999999999999,
            'S': -4.999999999999999
        },
        'bond_corr_length': {
            'Br': 8700.362592644753,
            'C': 133.44611217916807,
            'Cl': 984.7293895293759,
            'F': 98.47525641696103,
            'H': 0.9625400021075822,
            'N': 2.4696944019833944e-33,
            'O': 356.5621722725557,
            'S': 4254.993653344201
        },
        'bond_corr_neighbor': {
            'Br': -0.6360197371931731,
            'C': 0.07518742826453469,
            'Cl': 0.4135056554242813,
            'F': 0.44852850668999994,
            'H': -0.9999999999999999,
            'N': -0.2670986343093292,
            'O': -0.16328086552496884,
            'S': 0.11533434734503528
        },
        'mol_corr': -3.097820107831034
    },

    "LevelOfTheory(method='wb97xd3',basis='def2tzvp',software='qchem')": {
        'atom_corr': {
            'Br': -4.238722748476754,
            'C': 0.20073068139268807,
            'Cl': -2.5390084551621452,
            'F': -4.393361892652579,
            'H': -2.062168626045072,
            'N': -4.999999999999999,
            'O': -2.487093711352415,
            'S': -2.384672339052671
        },
        'bond_corr_length': {
            'Br': 2888.1231096339993,
            'C': 0.05944762961945064,
            'Cl': 257.4297204933608,
            'F': 136.98270149626455,
            'H': 1.0699994692879862,
            'N': 2.904232847702035e-28,
            'O': 120.01757300670776,
            'S': 301.64217902841733
        },
        'bond_corr_neighbor': {
            'Br': 0.27802934476159485,
            'C': -0.0945937593307584,
            'Cl': 0.17718518179957113,
            'F': 0.14692822191237273,
            'H': -0.17947642128291777,
            'N': -0.37012075875540995,
            'O': -0.07434692843236555,
            'S': -0.1353283919911719
        },
        'mol_corr': -3.781763592267793
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
#        [6] L.A. Curtiss, P.C. Redfern, K. Raghavachari, J. Chem. Phys. 2007, 126, 84108.

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
             "LevelOfTheory(method='b97d3',basis='def2msvp',software='qchem')": 1.014,  # [4]
             "LevelOfTheory(method='wb97xd',basis='augccpvtz',software='gaussian')": 0.988,  # [3], taken as 'ωB97X-D/maug-cc-pVTZ'
             "LevelOfTheory(method='wb97xd',basis='6311++g(d,p)',software='gaussian')": 0.988,  # [4]
             "LevelOfTheory(method='wb97xd',basis='def2tzvp',software='gaussian')": 0.988,  # [4]
             "LevelOfTheory(method='wb97xd',basis='def2svp',software='gaussian')": 0.986,  # [4]
             "LevelOfTheory(method='wb97xd3',basis='def2tzvp',software='qchem')": 0.984,  # [4]
             "LevelOfTheory(method='wb97mv',basis='def2tzvpd')": 1.002,  # [4]
             "LevelOfTheory(method='apfd',basis='def2tzvp')": 0.993,  # [4]
             "LevelOfTheory(method='apfd',basis='def2tzvpp')": 0.992,  # [4]
             "LevelOfTheory(method='mp2',basis='ccpvdz')": 0.953,  # [2]
             "LevelOfTheory(method='mp2',basis='ccpvtz')": 0.950,  # [2]
             "LevelOfTheory(method='mp2',basis='ccpvqz')": 0.962,  # [2]
             "LevelOfTheory(method='cbsqb3')": 0.99 * 1.014,  # [5], the 0.99 value is the ZPE scale factor of CBS-QB3
             "LevelOfTheory(method='cbsqb3paraskevas')": 0.99 * 1.014,  # [5], the 0.99 value is the ZPE scale factor of CBS-QB3
             "LevelOfTheory(method='cbsqb3rmg')": 0.99 * 1.014,  # [5], the 0.99 value is the ZPE scale factor of CBS-QB3
             "LevelOfTheory(method='g4')": 0.9854 * 1.014,  # [6], the 0.99 value is the ZPE scale factor of G4
             "LevelOfTheory(method='g4mp2')": 0.9854 * 1.014,  # [6], the 0.99 value is the ZPE scale factor of G4MP2
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
