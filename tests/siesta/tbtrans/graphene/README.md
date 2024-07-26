# Graphene TBtrans calculation

This is to test TBtrans siles.

- OS:
  Linux, Debian 12.
- Siesta (development version)
  5.1-MaX-42-gb6955e60a
- Uses the C.psml input file.

# Run

```shell
export SIESTA_PS_PATH=$(git rev-parse --show-toplevel)/static/siesta/PBE_sr_standard_05 
cd electrode
siesta electrode.fdf > RUN.out
cd ..
siesta run.fdf > RUN.out
cd ..
tbtrans run.fdf > TBT.out
```
