# H2O molecules

Simple test running H2O molecules setup so
there should be no dipole correction.

The test still has the dipole-correction enabled.

- OS:
  Linux, Debian 12.
- Siesta (development version)
  5.1-MaX-12-g8bcc883a9
- Uses the O.psml and H.psml input files.

# Run

```shell
SIESTA_PS_PATH=$(git rev-parse --show-toplevel)/static/siesta/PBE_sr_standard_05 siesta h2o_dipole.fdf > RUN.out
```
