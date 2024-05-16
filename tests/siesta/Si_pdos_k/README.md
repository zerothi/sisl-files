# Si PDOS calculations (k-points)

Do a k-point resolved PDOS calculation.

- OS:
  Linux, Debian 12.
- Siesta (development version)
  5.1-MaX-24-gc2193a788
- Uses the Si.psml input file.

# Run

```shell
SIESTA_PS_PATH=../../../static/siesta/PD_sr_standard_05 siesta Si_pdos.fdf > RUN.out
```
