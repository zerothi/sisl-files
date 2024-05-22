# Silicon wannierization using Siesta

- OS:
  Linux, Debian 12.
- Siesta (development version)
  5.1-MaX-24-gc2193a788
- Uses the Si.psml input file.
- Subsequent run with Wannier90 3.1.0

# Run

```shell
SIESTA_PS_PATH=../../../static/siesta/PD_sr_standard_05 siesta silicon.fdf > RUN_siesta.out
# The following might not work on case-insensitive OS
ln -s silicon.eigW silicon.eig
wannier90.x silicon > RUN_wannier.out
```
