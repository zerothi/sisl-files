# Pt dimer with SOC

- OS:
  Linux, Debian 12.
- Siesta (development version)
  5.1-MaX-24-gc2193a788
- Uses the Pt.psml input file.

# Run

```shell
SIESTA_PS_PATH=$(git rev-parse --show-toplevel)/static/siesta/PBE_fr_standard_04 siesta Pt2.fdf > RUN.out
```
