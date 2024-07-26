# 3 layer quintuple Bi2Se3 for spin-texture calculations

Used for:
- bands
- WFSX
- spin-texture

- OS:
  Linux, Debian 12.
- Siesta (development version)
  5.1-MaX-42-gb6955e60a
- Uses the Sr and Bi psml files

# Run

```shell
SIESTA_PS_PATH=$(git rev-parse --show-toplevel)/static/siesta/PBE_fr_standard_04 siesta Bi2Se3.fdf > RUN.out
```
