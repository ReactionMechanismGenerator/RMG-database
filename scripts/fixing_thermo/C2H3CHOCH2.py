#!/usr/bin/env python
# coding: utf-8

# # C2H3CHOCH2 (1-propen-1-one, 2-methyl) Thermochemistry
# 
# Note: Convert this .py into a .ipynb file by running `jupyter nbconvert --to notebook C2H3CHOCH2.py`
# or `jupytext --to notebook C2H3CHOCH2.py` or `jupytext --sync C2H3CHOCH2.py`.
# 
# Our goal is not to replace it with the best available thermo, because that could
# change the behavior of the models. We want to stay close to what was originally
# used.
# 
# The species is (SMILES `C=CC1CO1`)
# 
# ```
# multiplicity 2
# 1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
# 2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
# 3  C u0 p0 c0 {1,S} {4,D} {9,S}
# 4  C u0 p0 c0 {3,D} {10,S} {11,S}
# 5  O u0 p2 c0 {1,S} {2,S}
# 6  H u0 p0 c0 {1,S}
# 7  H u0 p0 c0 {2,S}
# 8  H u0 p0 c0 {2,S}
# 9  H u0 p0 c0 {3,S}
# 10 H u0 p0 c0 {4,S}
# 11 H u0 p0 c0 {4,S}
# ```
# 

# In[1]:


import copy
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
from rmgpy.chemkin import read_thermo_entry

# Importing rmgpy forces the non-interactive "Agg" matplotlib backend, so request
# the inline backend *after* that import to get figures embedded in the notebook.
get_ipython().run_line_magic('matplotlib', 'inline')

# Unit conversions: RMG thermo getters return SI (J/mol, J/mol/K).
CAL = 4.184           # J per cal      -> divide J/mol/K  by this for cal/mol/K
KCAL = 4184.0         # J per kcal     -> divide J/mol     by this for kcal/mol


# ## 1. Import the Chemkin thermo entries
# 
# `read_thermo_entry` returns the species label, a `NASA` object (two
# `NASAPolynomial` pieces — note the *high*-T polynomial is written first in the
# Chemkin format), and the elemental formula.
# 
# The `C2H3CHOCH2` entry (`A 8/83C`) is identical across JetSurF2,
# USC_Mech_ii and 2-BTP; we use the version with an explicit
# 1000 K join temperature.
# 
# A different NASA polynomial was presented here https://pubs.acs.org/doi/suppl/10.1021/acs.energyfuels.5c02454/suppl_file/ef5c02454_si_002.txt
# Revisiting the Combustion Kinetics of Di-Isopropyl Ketone: New Insights from Elevated Temperature LBV Measurements; Amardeep Fulzele, Aditya Kotwal, Sarvesh Patil, and Sudarshan Kumar; Energy & Fuels 2025 39 (34), 16254-16266; DOI: 10.1021/acs.energyfuels.5c02454
# 
# Which was also use originally by Lin Q in 10.1016/j.combustflame.2024.113614 with mech thermo  https://ars.els-cdn.com/content/image/1-s2.0-S0010218024003237-mmc5.txt
# 
# The original source of the competing updated NASA thermo was by Sun et al https://doi.org/10.1016/j.combustflame.2024.113614. Probing fuel-specific reaction intermediates from laminar premixed flames fueled by two C5 ketones and model interpretations
# ```
# C2H3CHOCH2              C   4H   6O   1         300.000 5000.000 1431.000      1  !\COMMENT:  
# +1.26762790E+01+1.40819509E-02-4.63473868E-06+7.01090838E-10-3.99438277E-14    2
# -4.08065264E+03-4.22515995E+01-3.59388437E+00+5.79063450E-02-4.97163294E-05    3
# +2.15818682E-08-3.69199072E-12+8.58852628E+02+4.28475443E+01+0.00000000E+00    4
# ```
# 
# It was later discovered that the base model was
# 
# AramcoMech1.3 and 2
# 
# ```
# C2H3CHOCH2              C   4H   6O   1    0G   300.000  5000.000 1431.000    11
#  1.26762790E+01 1.40819509E-02-4.63473868E-06 7.01090838E-10-3.99438277E-14    2
# -4.08065264E+03-4.22515995E+01-3.59388437E+00 5.79063450E-02-4.97163294E-05    3
#  2.15818682E-08-3.69199072E-12 8.58852628E+02 4.28475443E+01                   4
# ```
# 
# The conclusion of this analysis is that the NASA polynomial for the `C2H3CHOCH2` was updated in AramcoMech1.3 and 2, and not because the original measurement of AramcoMech1.3 was wrong, but it was incorrectly fitted as we found in this analysis that refitting the thermodynamic properties of the [supplementary material](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1002%2Fkin.20802&file=Supp_Mat_V9.pdf) presented in the AramcoMech1.0 publication aligns with the updated NASA in AramcoMech1.3 and 2.0.

# In[2]:


entry = """
C2H3CHOCH2        A 8/83C   4H   6O   1    0G   300.     3000.     1000.0      1
-4.72093360E+00 3.91413780E-02-6.52872650E-06-7.68209500E-09 2.51473310E-12    2
 1.75352252E+03 5.17190420E+01 7.97985440E-01 3.44034320E-02-1.24598510E-05    3
-5.18062790E-18 1.99359540E-21-6.48927540E+02 2.18896980E+01 1.00654250E+03    4
""".strip()


# In[3]:


read_thermo_entry(entry)


# In[4]:


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


# In[5]:


thermo0.polynomials


# In[6]:


comment = thermo0.comment


# Quick look at the (A 8/83) entry at the standard reference temperature, and the
# continuity gaps at the 1000 K join (where we expect trouble).

# In[7]:


T_REF = 298.15  # standard reference temperature for the "298 K" quantities

lo, hi = thermo0.polynomials
print(f"{species} ({comment}) at 298.15 K:")
print(f"  Cp = {lo.get_heat_capacity(T_REF) / CAL:8.3f} cal/mol/K")
print(f"   H = {lo.get_enthalpy(T_REF) / KCAL:8.3f} kcal/mol")
print(f"   S = {lo.get_entropy(T_REF) / CAL:8.3f} cal/mol/K")
print(f"\ncontinuity gaps at the {Tint:.0f} K join (low - high):")
print(f"  Cp: {(lo.get_heat_capacity(Tint) - hi.get_heat_capacity(Tint)) / CAL:+.4f} cal/mol/K")
print(f"   H: {(lo.get_enthalpy(Tint) - hi.get_enthalpy(Tint)) / KCAL:+.4f} kcal/mol")
print(f"   S: {(lo.get_entropy(Tint) - hi.get_entropy(Tint)) / CAL:+.4f} cal/mol/K")


# In[8]:


curran_entry = """
C2H3CHOCH2              C   4H   6O   1    0G   300.000  5000.000 1431.000     1
 1.26762790E+01 1.40819509E-02-4.63473868E-06 7.01090838E-10-3.99438277E-14    2
-4.08065264E+03-4.22515995E+01-3.59388437E+00 5.79063450E-02-4.97163294E-05    3
 2.15818682E-08-3.69199072E-12 8.58852628E+02 4.28475443E+01                   4
 """.strip()

curran_species, thermo_curran, curran_formula = read_thermo_entry(curran_entry)
curran_tint = thermo_curran.polynomials[0].Tmax.value_si
print(f"species : {curran_species}")
print(f"formula : {curran_formula}")
print(f"valid   : {thermo_curran.Tmin.value_si:.0f}-{thermo_curran.Tmax.value_si:.0f} K, "
      f"joined at {curran_tint:.0f} K")


# In[9]:


thermo_curran


# ## 2. Target data
# 
# Heat capacities at five temperatures, plus the 298 K enthalpy of formation and
# entropy. Each Cp point is associated with the polynomial that owns that
# temperature (≤ `Tint` → low-T piece, otherwise high-T piece); `Cp(1000 K)` sits
# exactly on the boundary and is assigned to the low-T piece.

# In[10]:


T_REF = 298.15  # standard reference temperature for the "298 K" quantities
Cp_T = np.array([300, 400.0, 500.0, 600.0, 800.0, 1000.0, 1500.0])   # K
Cp_target = np.array([19.87, 24.97 , 29.58, 33.69, 40.43, 45.19, 51.87])  # cal/mol/K.
H_target = 2.00   # kcal/mol  (ΔHf at 298 K)
S_target = 71.82   # cal/mol/K (S at 298 K)


# In[11]:


from rmgpy.molecule import Molecule
from rmgpy.thermo import ThermoData

m = Molecule(smiles='C=CC1CO1')   # matches the notebook's adjacency list


# In[12]:


display(m)


# In[13]:


td = ThermoData(
    Tdata=(Cp_T, 'K'),
    Cpdata=(Cp_target, 'cal/(mol*K)'),
    H298=(H_target, 'kcal/mol'),
    S298=(S_target, 'cal/(mol*K)'),
    Cp0=(m.calculate_cp0(), 'J/(mol*K)'),
    CpInf=(m.calculate_cpinf(), 'J/(mol*K)'),
)
nasa_new = td.to_nasa(Tmin=300.0, Tmax=3000.0, Tint=1000.0)


# In[14]:


new_nasa_tint = nasa_new.polynomials[0].Tmax.value_si


# ## 2. Plot Cp, H and S
# 
# Each polynomial piece is drawn over its own temperature range, so any
# discontinuity at the join shows up as a visible jump.

# In[15]:


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
    ("Cp", "Cp [cal/mol/K]", Cp_T, Cp_target),
    ("H", "H [kcal/mol]", np.array([T_REF]), np.array([H_target])),
    ("S", "S [cal/mol/K]", np.array([T_REF]), np.array([S_target])),
]
curve_sources = [
    (thermo0, Tint, "C0", f"{species} ({comment})"),
    (thermo_curran, curran_tint, "C1", f"{species} (AramcoMech2)"),
    (nasa_new, new_nasa_tint, "C2", f"{species} (New NASA from target data)"),
]
for ax, (prop, ylabel, T_pts, y_pts) in zip(axes, panels):
    for thermo, tint, color, label in curve_sources:
        T_lo, y_lo, T_hi, y_hi = curves(thermo, prop, tint)
        # Draw each piece over its own range, clipped to the plot limit.
        # Only the high piece carries the legend label (one entry per curve).
        for T_arr, y_arr, lab in ((T_lo, y_lo, None), (T_hi, y_hi, label)):
            mask = T_arr <= TMAX_PLOT
            ax.plot(T_arr[mask], y_arr[mask], color=color, lw=1.8, label=lab)
    ax.plot(T_pts, y_pts, "rs", ms=7, label="target", zorder=5)
    ax.axvline(Tint, color="k", lw=0.6, alpha=0.4)
    ax.set_xlim(right=TMAX_PLOT)
    ax.set_xlabel("T [K]")
    ax.set_ylabel(ylabel)
    ax.legend(fontsize=8)
fig.suptitle(f"{species} thermochemistry: {comment}", fontsize=11)
fig.tight_layout()
plt.show()


# In[16]:


def piece(thermo, T, tint=None):
    """Return the NASAPolynomial that owns temperature `T` (low-T owns the join).

    `tint` is the join temperature; it defaults to the published `Tint` (1000 K)
    but section 7 passes a different value to let the join float.
    """
    if tint is None:
        tint = Tint
    return thermo.polynomials[0] if T <= tint else thermo.polynomials[1]


# ## 3. Objective function: data residuals + soft continuity penalty
# 
# Every residual is made dimensionless by dividing by a fixed reference scale, so
# the terms are comparable and the objective is a clean sum of squares:
# 
# * **Data residuals** — relative error of each Cp point and of H(298), S(298).
# * **Continuity residuals** — the Cp, H and S gaps between the two polynomials at
#   `Tint`, normalised by fixed reference magnitudes (the target Cp(1000) and the
#   original H, S at `Tint`). A weight `w_cont` controls their importance.
# 
# Because Cp, H and S are all *linear* in the NASA coefficients and every
# denominator here is a constant, the objective is exactly quadratic in any single
# coefficient — which makes each 1-D optimization well-behaved.

# In[17]:


# Fixed reference magnitudes for normalising the continuity gaps (computed once
# from the original polynomial so they never change during fitting).
H_REF = abs(thermo0.polynomials[0].get_enthalpy(Tint) / KCAL)   # ~ kcal/mol at Tint
S_REF = abs(thermo0.polynomials[0].get_entropy(Tint) / CAL)     # ~ cal/mol/K at Tint

RESIDUAL_LABELS = (
    [f"Cp({T:.0f})" for T in Cp_T]
    + ["H(298)", "S(298)"]
    + ["cont:Cp", "cont:H", "cont:S"]
)


def residuals(thermo, w_cont=1.0, tint=None):
    """Vector of dimensionless residuals (data points then continuity gaps).

    `tint` is the join temperature where the two pieces meet and where the
    continuity gaps are measured; it defaults to the published `Tint` (1000 K).
    """
    if tint is None:
        tint = Tint
    w_cont = 10.0 # over-riding it here!
    lo, hi = thermo.polynomials
    r = [piece(thermo, T, tint).get_heat_capacity(T) / CAL / c - 1.0
         for T, c in zip(Cp_T, Cp_target)]
    r.append(lo.get_enthalpy(T_REF) / KCAL / H_target - 1.0)
    r.append(lo.get_entropy(T_REF) / CAL / S_target - 1.0)
    # continuity gaps at the join, normalised by fixed reference scales
    r.append(w_cont * (lo.get_heat_capacity(tint) - hi.get_heat_capacity(tint)) / CAL / Cp_target[3])
    r.append(w_cont * (lo.get_enthalpy(tint) - hi.get_enthalpy(tint)) / KCAL / H_REF)
    r.append(w_cont * (lo.get_entropy(tint) - hi.get_entropy(tint)) / CAL / S_REF)
    return np.array(r)


def objective(thermo, w_cont=1.0, tint=None):
    """Scalar least-squares objective: sum of squared residuals."""
    return float(np.sum(residuals(thermo, w_cont, tint) ** 2))


# How good is the published polynomial before we touch anything?

# In[18]:


def report(thermo, w_cont=1.0, tint=None):
    if tint is None:
        tint = Tint
    print(f"{'quantity':>10s}  {'model':>10s}  {'target':>10s}  {'rel.err':>9s}")
    for T, c in zip(Cp_T, Cp_target):
        m = piece(thermo, T, tint).get_heat_capacity(T) / CAL
        print(f"  Cp({T:5.0f})  {m:10.3f}  {c:10.3f}  {m / c - 1:+9.2%}")
    h = thermo.polynomials[0].get_enthalpy(T_REF) / KCAL
    s = thermo.polynomials[0].get_entropy(T_REF) / CAL
    print(f"   H(298)   {h:10.3f}  {H_target:10.3f}  {h / H_target - 1:+9.2%}")
    print(f"   S(298)   {s:10.3f}  {S_target:10.3f}  {s / S_target - 1:+9.2%}")
    lo, hi = thermo.polynomials
    print(f"\n  continuity gaps at {tint:.0f} K (low - high):")
    print(f"    Cp: {(lo.get_heat_capacity(tint) - hi.get_heat_capacity(tint)) / CAL:+.4f} cal/mol/K")
    print(f"     H: {(lo.get_enthalpy(tint) - hi.get_enthalpy(tint)) / KCAL:+.4f} kcal/mol")
    print(f"     S: {(lo.get_entropy(tint) - hi.get_entropy(tint)) / CAL:+.4f} cal/mol/K")
    print(f"\n  objective = {objective(thermo, w_cont, tint):.6f}")


report(thermo0)
OBJ0 = objective(thermo0)


# ## 4. Optimize each of the 14 coefficients independently
# 
# The 14 parameters are the 7 coefficients of each polynomial. In RMG's ordering
# `coeffs = [c0, c1, c2, c3, c4, c5, c6]`:
# 
# * `c0…c4` set the Cp(T) = R·(c0 + c1T + c2T² + c3T³ + c4T⁴) shape,
# * `c5` is the enthalpy integration constant (shifts H),
# * `c6` is the entropy integration constant (shifts S).
# 
# Each coefficient is allowed to vary **freely** — far from its starting value and
# across zero if that helps — so a coefficient that starts at ~1e-19 is not
# confined to stay tiny. To keep all 14 searches numerically well-conditioned
# despite the coefficients spanning ~22 orders of magnitude, we optimize a
# perturbation `delta` measured in units of each coefficient's *natural* scale
# (the value that makes a unit change produce an O(1) change in Cp/R, H/R or S/R),
# which is set by the coefficient's role in the polynomial — **not** by its
# starting magnitude. The optimizer (`scipy.optimize.minimize_scalar`, unbounded
# Brent) is then free to send `delta` anywhere.

# In[19]:


# Enumerate the 14 parameters as (polynomial index, coefficient index).
PARAMS = [(p, i) for p in (0, 1) for i in range(7)]
PARAM_NAMES = [f"{'low' if p == 0 else 'high'} c{i}" for p, i in PARAMS]

# Natural scale of each coefficient, independent of its starting value. In
# Cp/R = c0 + c1·T + c2·T² + c3·T³ + c4·T⁴, coefficient cᵢ multiplies Tⁱ, so its
# natural size is Tref^(-i); c5 is the H/R offset (units of K ~ Tref) and c6 is
# the dimensionless S/R offset (~1).
TREF = 1000.0


def natural_scale(i):
    if i <= 4:
        return TREF ** (-i)
    return TREF if i == 5 else 1.0


def optimize_single(p, i, w_cont=1.0):
    """Optimize only coefficient `i` of polynomial `p`, starting from the original.

    Returns a fresh NASA object that differs from `thermo0` in exactly one
    coefficient (the original is never mutated).
    """
    thermo = copy.deepcopy(thermo0)
    v0 = thermo0.polynomials[p].coeffs[i]
    scale = natural_scale(i)  # fixed scale, independent of the starting value

    def set_value(value):
        coeffs = thermo.polynomials[p].coeffs.copy()
        coeffs[i] = value
        thermo.polynomials[p].coeffs = coeffs

    def f(delta):
        set_value(v0 + delta * scale)
        return objective(thermo, w_cont)

    # Unbounded Brent: delta may grow large and cross zero, so the coefficient is
    # free to change sign and move orders of magnitude from where it started.
    res = minimize_scalar(f, method="brent")
    set_value(v0 + res.x * scale)  # leave `thermo` holding the optimum
    return thermo, v0, thermo.polynomials[p].coeffs[i], res.fun


def objective_vs_tint(tint, w_cont=1.0):
    """Objective of the *original* polynomial as a function of the join `tint`."""
    return objective(thermo0, w_cont, tint)


def optimize_tint(w_cont=1.0, n_grid=2000):
    """Optimize only the join temperature, the 15th parameter, with all 14
    coefficients held at their published values.

    Moving the join changes two things: (a) which polynomial piece owns each Cp
    data point, and (b) the temperature at which the continuity gaps are
    measured. Effect (a) makes the objective piecewise — it jumps each time
    `tint` crosses one of the Cp data temperatures — so a single Brent search
    could land in the wrong piece. We therefore scan a dense grid across the
    full validity range for the global region, then refine locally with a
    bounded search inside the smooth interval around the grid winner.

    Returns a fresh NASA object whose join boundary has been moved to the
    optimum (the original `thermo0` is never mutated).
    """
    thermo = copy.deepcopy(thermo0)
    lo, hi = thermo.polynomials
    t_min = thermo0.Tmin.value_si
    t_max = thermo0.Tmax.value_si

    grid = np.linspace(t_min + 1.0, t_max - 1.0, n_grid)
    vals = np.array([objective(thermo, w_cont, t) for t in grid])
    t_seed = grid[int(np.argmin(vals))]

    # Refine within one grid step of the winner, staying inside one smooth piece.
    step = grid[1] - grid[0]
    res = minimize_scalar(lambda t: objective(thermo, w_cont, t),
                          method="bounded", bounds=(t_seed - step, t_seed + step))
    t_opt = res.x if res.fun <= objective(thermo, w_cont, t_seed) else t_seed

    # Leave `thermo` holding the optimum: move the shared join boundary so the
    # returned object is self-consistent (its own select_polynomial uses t_opt).
    lo.Tmax = (t_opt, "K")
    hi.Tmin = (t_opt, "K")
    return thermo, Tint, t_opt, objective(thermo, w_cont, t_opt)


results = []
for (p, i), name in zip(PARAMS, PARAM_NAMES):
    thermo_opt, v_old, v_new, obj = optimize_single(p, i)
    results.append({"name": name, "p": p, "i": i, "thermo": thermo_opt,
                    "v_old": v_old, "v_new": v_new, "obj": obj, "tint": Tint})

# Sanity check: the original object was never modified.
assert objective(thermo0) == OBJ0

# The 15th parameter: the join temperature itself (see section 7 for the full
# landscape). We append it to `results` so the summary table, bar chart and
# per-fit plots below treat it on the same footing as the 14 coefficients.
thermo_tint, t_old, t_new, obj_tint = optimize_tint()
results.append({"name": "Tint", "p": None, "i": None, "thermo": thermo_tint,
                "v_old": t_old, "v_new": t_new, "obj": obj_tint, "tint": t_new})


# ## 5. Summary: which single parameter helps the most?
# 
# The table and bar chart below rank all **15** single-parameter fits — the 14
# coefficients plus the join temperature `Tint`. For `Tint` the "old/new value"
# columns are temperatures in K rather than coefficient values.

# In[20]:


order = sorted(range(len(results)), key=lambda k: results[k]["obj"])
print(f"original objective = {OBJ0:.6f}\n")
print(f"{'parameter':>10s}  {'old value':>13s}  {'new value':>13s}  {'objective':>10s}  {'reduction':>9s}")
for k in order:
    r = results[k]
    print(f"{r['name']:>10s}  {r['v_old']:13.4e}  {r['v_new']:13.4e}  "
          f"{r['obj']:10.6f}  {1 - r['obj'] / OBJ0:+9.1%}")


# In[21]:


fig, ax = plt.subplots(figsize=(9, 4.5))
names = [results[k]["name"] for k in order]
objs = [results[k]["obj"] for k in order]
ax.bar(range(len(objs)), objs, color="steelblue")
ax.axhline(OBJ0, color="crimson", ls="--", label=f"original = {OBJ0:.4f}")
ax.set_xticks(range(len(names)))
ax.set_xticklabels(names, rotation=45, ha="right")
ax.set_ylabel("objective (sum of squared residuals)")
ax.set_title("Best achievable objective when varying one parameter at a time")
ax.legend()
fig.tight_layout()
plt.show()


# ## 6. Cp, H and S curves for each single-parameter fit
# 
# For every parameter we plot the resulting Cp, H and S curves (solid) against the
# original polynomial (grey dashed) and the target data (markers). Each polynomial
# piece is drawn over its own temperature range, so any discontinuity at the join
# shows up as a visible jump. The last figure is the `Tint` fit: the two original
# pieces are unchanged but the join (black line) has moved off 1000 K.

# In[22]:


def curves(thermo, prop, tint=None):
    """Evaluate a property ('Cp', 'H', 'S') over each polynomial's own range.

    The low piece is drawn over [Tmin, tint] and the high piece over [tint, Tmax],
    so moving the join (the 15th parameter) is reflected directly in the split.
    Returns the four arrays (T_lo, y_lo, T_hi, y_hi).
    """
    if tint is None:
        tint = Tint
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


def plot_fit(result):
    """Three-panel Cp/H/S comparison for one single-parameter fit."""
    thermo = result["thermo"]
    tint = result.get("tint", Tint)
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    panels = [
        ("Cp", "Cp [cal/mol/K]", Cp_T, Cp_target),
        ("H", "H [kcal/mol]", np.array([T_REF]), np.array([H_target])),
        ("S", "S [cal/mol/K]", np.array([T_REF]), np.array([S_target])),
    ]
    for ax, (prop, ylabel, T_pts, y_pts) in zip(axes, panels):
        oT_lo, o_lo, oT_hi, o_hi = curves(thermo0, prop)          # original join (1000 K)
        nT_lo, n_lo, nT_hi, n_hi = curves(thermo, prop, tint)     # this fit's join
        ax.plot(oT_lo, o_lo, color="grey", ls="--", lw=1)
        ax.plot(oT_hi, o_hi, color="grey", ls="--", lw=1, label="original")
        ax.plot(nT_lo, n_lo, color="C0", lw=1.8)
        ax.plot(nT_hi, n_hi, color="C0", lw=1.8, label="optimized")
        ax.plot(T_pts, y_pts, "rs", ms=7, label="target", zorder=5)
        ax.axvline(tint, color="k", lw=0.6, alpha=0.4)
        ax.set_xlabel("T [K]")
        ax.set_ylabel(ylabel)
        ax.legend(fontsize=8)
    fig.suptitle(f"Vary '{result['name']}':  {result['v_old']:.4e} → "
                 f"{result['v_new']:.4e}   |   objective {OBJ0:.5f} → {result['obj']:.5f}",
                 fontsize=11)
    fig.tight_layout()
    plt.show()


for result in results:
    plot_fit(result)


# ## 7. The 15th parameter: a floating join temperature
# 
# So far the join between the two polynomial pieces has been fixed at the
# published `Tint = 1000 K`. Here we treat that join as the **15th optimizable
# parameter** and ask the same sensitivity question: *holding all 14 coefficients
# at their published values, where should the two pieces meet to fit the data
# best?*
# 
# This is qualitatively different from moving a coefficient. The two polynomials
# are unchanged; we only slide the temperature at which we switch from one to the
# other. That changes the objective in two ways:
# 
# * **which piece owns a Cp point** — as `Tint` sweeps past one of the Cp data
#   temperatures, that point is suddenly evaluated on the *other* polynomial,
#   producing a step in the objective;
# * **where continuity is enforced** — the Cp/H/S gaps in the penalty are measured
#   at the join, and the two pieces drift apart away from 1000 K.
# 
# The result is a piecewise objective with kinks/jumps at each Cp data
# temperature, which is why `optimize_tint` scans a dense grid before refining.

# In[23]:


report(thermo_tint, tint=t_new)
print(f"\njoin temperature: {t_old:.1f} K -> {t_new:.1f} K")
print(f"objective: {OBJ0:.6f} -> {obj_tint:.6f}  ({1 - obj_tint / OBJ0:+.1%})")


# ## Conclusion
# There is no single parameter typo that can fix the inconsistencies in the thermodynamic data.
# Let's instead replace the Cp(T) curves with more reliable ones, but preserve the H and S values that these models might rely on

# In[24]:


from rmgpy.thermo import ThermoData

R = 8.314462618  # J/mol/K
# Ideal-gas Cp limits for C4H6O (11 atoms, nonlinear):
#   Cp0   = 4R           (T -> 0)
#   CpInf = (3N-2)R = 31R (T -> inf)
td = ThermoData(
    Tdata=(Cp_T, 'K'),
    Cpdata=(Cp_target, 'cal/(mol*K)'),
    H298=(H_target, 'kcal/mol'),
    S298=(S_target, 'cal/(mol*K)'),
    Cp0=(4 * R, 'J/(mol*K)'),
    CpInf=(31 * R, 'J/(mol*K)'),
)

nasa_new = td.to_nasa(Tmin=300.0, Tmax=3000.0, Tint=1000.0)  # continuity=3 by default


# In[25]:


nasa_new


# In[26]:


import cantera as ct

hi = list(nasa_new.polynomials[1].coeffs)   # high-T piece
lo = list(nasa_new.polynomials[0].coeffs)   # low-T piece
coeffs = [1000.0] + hi + lo                 # NasaPoly2 order: [Tmid, high(7), low(7)]

sp = ct.Species('C2H3CHOCH2', {'C': 4, 'H': 6, 'O': 1})
sp.thermo = ct.NasaPoly2(300.0, 3000.0, ct.one_atm, coeffs)
# sp.thermo.cp(T)/sp.thermo.h(T)/sp.thermo.s(T) or drop into a Solution to check


# In[ ]:




