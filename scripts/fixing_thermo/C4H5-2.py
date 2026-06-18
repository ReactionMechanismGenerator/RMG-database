# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: rmg_env18
#     language: python
#     name: python3
# ---

# %% [markdown]
# # C4H5-2 (1-methylpropargyl / but-2-yn-1-yl radical) Thermochemistry
#
# Note: Convert this .py into a .ipynb file by running `jupyter nbconvert --to notebook C4H5-2.py`
# or `jupytext --to notebook C4H5-2.py` or `jupytext --sync C4H5-2.py`.
#
# This is the radical analogue of the [C4H6-2](C4H6-2.py) exercise. Many models
# carry a `C4H5-2` thermo entry tagged `H6W/94` that also has a
# discontinuity at the 1000 K join and errors in Cantera. We're investigating.
#
# Our goal is not to replace it with the best available thermo, because that could
# change the behavior of the models. We want to stay close to what was originally
# used.
#
# The species is `[CH2]C#CC` (SMILES `CC#C[CH2]`), i.e. CH3-C#C-*CH2, the
# but-2-yn-1-yl (1-methylpropargyl) radical:
#
# ```
# multiplicity 2
# 1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
# 2 C u1 p0 c0 {4,S} {8,S} {9,S}
# 3 C u0 p0 c0 {1,S} {4,T}
# 4 C u0 p0 c0 {2,S} {3,T}
# 5 H u0 p0 c0 {1,S}
# 6 H u0 p0 c0 {1,S}
# 7 H u0 p0 c0 {1,S}
# 8 H u0 p0 c0 {2,S}
# 9 H u0 p0 c0 {2,S}
# ```
#
# The identical `H6W/94` entry appears in JetSurF2, mch_chx_v8b_therm,
# AramcoMech1.3, and USC_Mech_ii. The `H6W/94` tag points to Hai Wang & co-workers
# (the "H6W" prefix shows up throughout the USC-Mech family); `94` is presumably
# 1994.
#
# We also load the entry from CurranPentane for comparison.
#

# %%
import numpy as np
import matplotlib.pyplot as plt

from rmgpy.chemkin import read_thermo_entry

# Importing rmgpy forces the non-interactive "Agg" matplotlib backend, so request
# the inline backend *after* that import to get figures embedded in the notebook.
# %matplotlib inline

# Unit conversions: RMG thermo getters return SI (J/mol, J/mol/K).
CAL = 4.184           # J per cal      -> divide J/mol/K  by this for cal/mol/K
KCAL = 4184.0         # J per kcal     -> divide J/mol     by this for kcal/mol

# %% [markdown]
# ## 1. Import the Chemkin thermo entries
#
# `read_thermo_entry` returns the species label, a `NASA` object (two
# `NASAPolynomial` pieces — note the *high*-T polynomial is written first in the
# Chemkin format), and the elemental formula.
#
# The `C4H5-2` entry (`H6W/94`) is identical across JetSurF2, AramcoMech1.3,
# USC_Mech_ii and mch_chx_v8b_therm; we use the version with an explicit
# 1000 K join temperature.

# %%
entry = """
C4H5-2            H6W/94C   4H   5    0    0G   300.000  3000.00  1000.00      1
 1.45381710E+01-8.56770560E-03 2.35595240E-05-1.36763790E-08 2.44369270E-12    2
 3.32590950E+04-4.53694970E+01 2.96962800E+00 2.44422450E-02-9.12514240E-06    3
-4.24668710E-18 1.63047280E-21 3.55033160E+04 1.20360510E+01 3.73930550E+04    4
""".strip()

species, thermo0, formula = read_thermo_entry(entry)

# The published lower limit is 300 K; lower it to 298 K (as RMG's import does) so
# the polynomial can be evaluated at the standard 298.15 K reference.
thermo0.Tmin = (298.0, "K")
thermo0.polynomials[0].Tmin = (298.0, "K")

Tint = thermo0.polynomials[0].Tmax.value_si  # common temperature where the two polys meet (1000 K)

print(f"species : {species}")
print(f"formula : {formula}")
print(f"valid   : {thermo0.Tmin.value_si:.0f}-{thermo0.Tmax.value_si:.0f} K, joined at Tint = {Tint:.0f} K")
print(f"low-T  coeffs (298-{Tint:.0f} K): {thermo0.polynomials[0].coeffs}")
print(f"high-T coeffs ({Tint:.0f}-{thermo0.Tmax.value_si:.0f} K): {thermo0.polynomials[1].coeffs}")

# %% [markdown]
# The CurranPentane `C4H5` entry, for comparison.
#
# Reportedly used in 
# An ignition delay time and chemical kinetic modeling study of the pentane isomers
# John Bugler, Brandon Marks, Olivier Mathieu, Rachel Archuleta, Alejandro Camou, Claire Gregoire, Karl A. Heufer, Eric L. Petersen, Henry J. Curran
# Combustion and Flame, 2016, 163, 138-156  https://doi.org/10.1016/j.combustflame.2015.09.014
#
#
# Also found in Ahfaz Ahmed, William J. Pitz, Carlo Cavallotti, Marco Mehl, Nitin Lokachari, Elna J.K. Nilsson, Jui-Yang Wang, Alexander A. Konnov, Scott W. Wagnon, Bingjie Chen, Zhandong Wang, Seonah Kim, Henry J. Curran, Stephen J. Klippenstein, William L. Roberts, S. Mani Sarathy,
# Small ester combustion chemistry: Computational kinetics and experimental study of methyl acetate and ethyl acetate,
# Proceedings of the Combustion Institute, Volume 37, Issue 1, 2019, Pages 419-428, https://doi.org/10.1016/j.proci.2018.06.178
#

# %% [markdown]
#

# %%
curran_entry = """
C4H5                    C   4H   5          G   200.000  5000.000 1385.00      1
 1.03231000E+01 1.17626000E-02-4.00005000E-06 6.18728000E-10-3.58084000E-14    2
 3.25861000E+04-2.88794000E+01 2.31011000E+00 2.83747000E-02-1.63837000E-05    3
 4.46252000E-09-4.30511000E-13 3.55843000E+04 1.49106000E+01                   4
 """.strip()

curran_species, thermo_curran, curran_formula = read_thermo_entry(curran_entry)
curran_tint = thermo_curran.polynomials[0].Tmax.value_si
print(f"species : {curran_species}")
print(f"formula : {curran_formula}")
print(f"valid   : {thermo_curran.Tmin.value_si:.0f}-{thermo_curran.Tmax.value_si:.0f} K, "
      f"joined at {curran_tint:.0f} K")

# %% [markdown]
# Quick look at the H6W/94 entry at the standard reference temperature, and the
# continuity gaps at the 1000 K join (where we expect trouble).

# %%
T_REF = 298.15  # standard reference temperature for the "298 K" quantities

lo, hi = thermo0.polynomials
print(f"C4H5-2 (H6W/94) at 298.15 K:")
print(f"  Cp = {lo.get_heat_capacity(T_REF) / CAL:8.3f} cal/mol/K")
print(f"   H = {lo.get_enthalpy(T_REF) / KCAL:8.3f} kcal/mol")
print(f"   S = {lo.get_entropy(T_REF) / CAL:8.3f} cal/mol/K")
print(f"\ncontinuity gaps at the {Tint:.0f} K join (low - high):")
print(f"  Cp: {(lo.get_heat_capacity(Tint) - hi.get_heat_capacity(Tint)) / CAL:+.4f} cal/mol/K")
print(f"   H: {(lo.get_enthalpy(Tint) - hi.get_enthalpy(Tint)) / KCAL:+.4f} kcal/mol")
print(f"   S: {(lo.get_entropy(Tint) - hi.get_entropy(Tint)) / CAL:+.4f} cal/mol/K")

# %% [markdown]
# ## 2. Plot Cp, H and S
#
# Each polynomial piece is drawn over its own temperature range, so any
# discontinuity at the join shows up as a visible jump.

# %%
def curves(thermo, prop, tint):
    """Evaluate a property ('Cp', 'H', 'S') over each polynomial's own range.

    The low piece is drawn over [Tmin, tint] and the high piece over [tint, Tmax].
    Returns the four arrays (T_lo, y_lo, T_hi, y_hi).
    """
    lo, hi = thermo.polynomials
    T_lo = np.linspace(thermo.Tmin.value_si, tint, 200)
    T_hi = np.linspace(tint, thermo.Tmax.value_si, 200)
    if prop == "Cp":
        f, sc = "get_heat_capacity", CAL
    elif prop == "H":
        f, sc = "get_enthalpy", KCAL
    else:
        f, sc = "get_entropy", CAL
    y_lo = np.array([getattr(lo, f)(T) / sc for T in T_lo])
    y_hi = np.array([getattr(hi, f)(T) / sc for T in T_hi])
    return T_lo, y_lo, T_hi, y_hi


TMAX_PLOT = 3000.0
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
panels = [
    ("Cp", "Cp [cal/mol/K]"),
    ("H", "H [kcal/mol]"),
    ("S", "S [cal/mol/K]"),
]
curve_sources = [
    (thermo0, Tint, "C0", "C4H5-2 (H6W/94)"),
    (thermo_curran, curran_tint, "C1", "C4H5 (CurranPentane)"),
]
for ax, (prop, ylabel) in zip(axes, panels):
    for thermo, tint, color, label in curve_sources:
        T_lo, y_lo, T_hi, y_hi = curves(thermo, prop, tint)
        # Draw each piece over its own range, clipped to the plot limit.
        # Only the high piece carries the legend label (one entry per curve).
        for T_arr, y_arr, lab in ((T_lo, y_lo, None), (T_hi, y_hi, label)):
            mask = T_arr <= TMAX_PLOT
            ax.plot(T_arr[mask], y_arr[mask], color=color, lw=1.8, label=lab)
    ax.axvline(Tint, color="k", lw=0.6, alpha=0.4)
    ax.set_xlim(right=TMAX_PLOT)
    ax.set_xlabel("T [K]")
    ax.set_ylabel(ylabel)
    ax.legend(fontsize=8)
fig.suptitle("C4H5-2 thermochemistry: H6W/94 vs. CurranPentane C4H5", fontsize=11)
fig.tight_layout()
plt.show()

# %% [markdown]
# ## 3. Differences between CurranPentane and H6W/94
#
# CurranPentane is the same isomer and tracks H6W/94 closely at low temperature, so
# plot the difference (CurranPentane − H6W/94) in H, S and G as a function of
# temperature, up to 3000 K (the H6W/94 validity limit). Each `NASA` object selects
# the correct polynomial piece for every T, so these curves span both pieces of
# each entry — and the H6W/94 discontinuity at its 1000 K join shows up as a kink.

# %%
T_diff = np.linspace(T_REF, TMAX_PLOT, 300)
dH = np.array([(thermo_curran.get_enthalpy(T) - thermo0.get_enthalpy(T)) / KCAL for T in T_diff])
dS = np.array([(thermo_curran.get_entropy(T) - thermo0.get_entropy(T)) / CAL for T in T_diff])
dG = np.array([((thermo_curran.get_enthalpy(T) - T * thermo_curran.get_entropy(T))
                - (thermo0.get_enthalpy(T) - T * thermo0.get_entropy(T))) / KCAL for T in T_diff])

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, y, ylabel in zip(
    axes,
    (dH, dS, dG),
    ("ΔH [kcal/mol]", "ΔS [cal/mol/K]", "ΔG [kcal/mol]"),
):
    ax.plot(T_diff, y, color="C3", lw=1.8)
    ax.axhline(0.0, color="grey", ls=":", lw=1)
    ax.axvline(Tint, color="k", lw=0.6, alpha=0.4)
    ax.set_xlabel("T [K]")
    ax.set_ylabel(ylabel)
fig.suptitle("CurranPentane C4H5 − H6W/94 C4H5-2 differences vs. T", fontsize=11)
fig.tight_layout()
plt.show()

# %% [markdown]
# # Conclusion
# The Curran Pentane entry for C4H5 is very similar to the probelmatic one used in JetSurF2, AramcoMech1.3,
# USC_Mech_ii. It even has the same attribution (`H6W/94`). The match below 1000K is identical. So let's just use the CurranPentane entry.
# Its source is An ignition delay time and chemical kinetic modeling study of the pentane isomers
# John Bugler, Brandon Marks, Olivier Mathieu, Rachel Archuleta, Alejandro Camou, Claire Gregoire, Karl A. Heufer, Eric L. Petersen, Henry J. Curran
# Combustion and Flame, 2016, 163, 138-156  https://doi.org/10.1016/j.combustflame.2015.09.014
#

# %%
