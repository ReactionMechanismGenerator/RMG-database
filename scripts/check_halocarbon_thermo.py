#!/usr/bin/env python3
"""
Check CHO*_G4 thermo libraries for entries with >14 atoms and a
"Hindered Rotor" reference string, which may indicate results that
warrant closer inspection for large molecules.

Writes a CSV to scripts/check_halocarbon_thermo.csv and prints
WARNING entries to stdout.

There is concern that Gaussian was not run with iop(2/9=2000)
which means that when there are 14 or more atoms, the Hessian 
is output in a different coordinate system from the geometry,
which can lead to incorrect frequencies when projecting out
the hindered rotors, which can lead to erroneous entropy values
and hence bad Gibbs energies.
See https://github.com/ReactionMechanismGenerator/RMG-Py/pull/2758
and https://github.com/ReactionMechanismGenerator/RMG-Py/issues/2757
"""

import csv
import re
from pathlib import Path

repo_root = Path(__file__).parent.parent
lib_dir = repo_root / "input" / "thermo" / "libraries"
output_csv = Path(__file__).parent / "check_halocarbon_thermo.csv"

files = sorted(lib_dir.glob("CHO*_G4.py"))
if not files:
    raise FileNotFoundError(f"No CHO*_G4.py files found in {lib_dir}")

index_re = re.compile(r'index\s*=\s*(\d+)')
label_re = re.compile(r'label\s*=\s*["\']([^"\']*)["\']')
molecule_re = re.compile(r'molecule\s*=\s*"""(.*?)"""', re.DOTALL)
# Avoid matching referenceType by requiring only whitespace then = after 'reference'
reference_re = re.compile(r'(?<!\w)reference\s*=\s*["\']([^"\']*)["\']')
# Atom lines look like:  "1  Br u0 ..." or "14 H  u0 ..."
atom_line_re = re.compile(r'^\s*\d+\s+[A-Z]', re.MULTILINE)

rows = []

for filepath in files:
    text = filepath.read_text()
    # Split on entry( at the start of a line; first chunk is the file header
    chunks = re.split(r'^entry\(', text, flags=re.MULTILINE)
    for chunk in chunks[1:]:
        idx_m = index_re.search(chunk)
        label_m = label_re.search(chunk)
        mol_m = molecule_re.search(chunk)
        ref_m = reference_re.search(chunk)

        if not all([idx_m, label_m, mol_m, ref_m]):
            continue

        index = int(idx_m.group(1))
        label = label_m.group(1)
        molecule_block = mol_m.group(1)
        reference = ref_m.group(1)

        num_atoms = len(atom_line_re.findall(molecule_block))
        warning = num_atoms > 13 and "Hindered Rotor" in reference

        rows.append({
            "index": index,
            "label": label,
            "num_atoms": num_atoms,
            "reference": reference,
            "WARNING": warning,
            # kept internally for stdout reporting, not written to CSV
            "_file": filepath.name,
        })

# Write CSV (rename _file → file for output)
for r in rows:
    r["file"] = r.pop("_file")

fieldnames = ["file", "index", "label", "num_atoms", "reference", "WARNING"]
with open(output_csv, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {len(rows)} entries to {output_csv}\n")

# Report warnings to stdout
warnings = [r for r in rows if r["WARNING"]]
if not warnings:
    print("No WARNING entries found.")
else:
    print(f"{len(warnings)} WARNING entries (>13 atoms + 'Hindered Rotor' in reference):\n")
    current_file = None
    for r in sorted(warnings, key=lambda x: (x["file"], x["index"])):
        if r["file"] != current_file:
            current_file = r["file"]
            print(f"  {current_file}")
        print(f"    index={r['index']:>4}  atoms={r['num_atoms']:>2}  {r['label']}")
