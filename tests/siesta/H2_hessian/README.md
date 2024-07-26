# H2 molecule for hessian calculation

Simple test running H2 molecule for creating
the force-constants.

- OS:
  Linux, Debian 12.
- Siesta (development version)
  5.1-MaX-22-g14d40d4d4
- Uses the H.psml input file.

# Run

```shell
SIESTA_PS_PATH=$(git rev-parse --show-toplevel)/static/siesta/PBE_sr_standard_05 siesta h2_hessian.fdf > RUN.out
```
