----
481
----

[185] Roth, W.R.; Scholz, B.P.; Breuckmann, R.; Jelich, K.; Lennartz, H-W. *Chem. Ber.* 1982, 115, 1934. 

CH2=CHC(=CH2)C(=CH2)CH-CH2 --> cyclobutene, 1,2-diethenyl. 

(Apparently, reaction of 4->5; doesn't seem to be a birad recombination; 

note similar reaction in reference 6

Data derived from fitting to a complex mechanism. Excitation: thermal, analysis: GC. Pressure 0.01-0.77 atm.

***Should probably be removed, as this does not fit with this reaction family*** GRM: I have commented it out for the time-being; the reaction that might actually be relevant here is 2->13 (Abb. 1)

Verified by Greg Magoon (with translation help from CFG); Barrier, DA, and DE0 changed based on Gl. 8 on p. 1937; I didn't check if this was high-pressure limit

----
482
----

[186] Benson, S.W. J. Chem. Phys. 1967, 46, 4920.

CH2=CHCH(.)CH2CH2CH(.)CH=CH2 --> 4-vinylcyclohexene. (Rxn. -c); arises from birad recombination of resonance isomer: .CH2CH=CHCH2CH2CH(.)CH=CH2

Data are estimated.

***this only considers cis-cis isomer reaction*** cis-trans A prefactor is 50% of the value used here; also, on p. 4923, it is stated that cis trans rate is 5/6 of the overall rate, so maybe the k that should be used is 0.6 of the value currently in place?
Verified by Greg Magoon: Rxn. -d. also looks to be of interest here; whether the rate is high-pressure limit was not investigated, but p. 4922 says that pressures involved were low; DE0 uncertainty added; regarding temperature range, I considered dropping lower temperature limit from 550 K to 400 K (based on p. 4923), but it seems that experiments were performed at or around 600 K, so I will leave it at 550-650 K

Note: after some preliminary confusion on my part, it looks like the existing groups are correct (the correct resonance form for the CH2 radical is taken into account with the Ypri_rad_out (i.e. Cpri_rad_out_H2)), but arguably, another, a more-specific group (C_rad_out_H2/OneDe and Cpri_rad_out_H2/OneDe) should be specified to account for delocalizing group at this site

----
483
----

[187] Grimme, W.; Schumachers, L.; Roth, W.R.; Breuckmann, R. Chem. Ber. 1981, 114, 3197. 

(E)-CH2=CHCH=CHCH=CH2 --> 1,3-cyclohexadiene.

***Reference doesn't have this reaction***

Absolute value measured directly. Excitation: thermal, analysis: GC.

Checked by Greg Magoon: this reference doesn't seem to have this reaction, and even if it did, it wouldn't be biradical recombination; therefore, I have commented this entry out; there are some (polycyclic) birad recombinations and ring opening reactions in the paper, however

---
484
---

[188] Lewis, K.E.; Steiner, H. J. Chem. Soc. 1964, 3080.

(Z)-CH2=CHCH=CHCH=CH2 --> 1,3-cyclohexadiene.

Absolute value measured directly. Excitation: thermal, analysis: Vis-UV. Pressure0.08-0.11 atm.

***Should probably be removed, as this does not seem to fit with this reaction family***
Checked by Greg Magoon: this reference does not seem to consider biradical form; as far as I can tell, they are considering "regular" 1,3,5-hexatriene (not diradical excited state)

----
484
----

[x] Sirjean, B.; Glaude, P. A.; Ruiz-Lopez, M. F.; Fournet, R.; J. Phys. Chem. A. 2006, 110, 12693-12704. 
http://dx.doi.org/10.1021/jp0651081
.CH2CH2CH2CH2. -> cyclobutane (k2-1 in Scheme 3/Table 3)

TST calculation

Added by Greg Magoon: Stated pressure is 1 atm, but I believe they are actually calculating the high-pressure limit rate constant

----
485
----

[x] Sirjean, B.; Glaude, P. A.; Ruiz-Lopez, M. F.; Fournet, R.; J. Phys. Chem. A. 2006, 110, 12693-12704. 
http://dx.doi.org/10.1021/jp0651081
.CH2CH2CH2CH2CH2. -> cyclopentane (k4-1 in Scheme 5/Table 7)

TST calculation

Added by Greg Magoon: Stated pressure is 1 atm, but I believe they are actually calculating the high-pressure limit rate constant

----
486
----

[x] Sirjean, B.; Glaude, P. A.; Ruiz-Lopez, M. F.; Fournet, R.; J. Phys. Chem. A. 2006, 110, 12693-12704. 
http://dx.doi.org/10.1021/jp0651081
.CH2CH2CH2CH2CH2CH2. -> cyclohexane (k5-1+k5-2 in Scheme 7/Table 10) (includes formation of both boat and chair conformations)

TST calculation

Added by Greg Magoon: Stated pressure is 1 atm, but I believe they are actually calculating the high-pressure limit rate constant; the rate constant added here was found my performing least squares fit for log(ktot) from 600-2000 K (where ktot is the sum of k5-1 and k5-2)

Note: Recent experimental/RRKM study by Kiefer, Gupte, Harding, and Klippenstein (http://www.combustion.org.uk/ECM_2009/P810069.pdf) (stated uncertainty is +/- 30%) appears to agree with Sirjean et al. results, but they only report forward rate constant