# SrTiO3 3D structure


Used for:
- bands
- PDOS
- RHO

And in 3 configurations:
- unpolarized
- polarized
- non-collinear

- OS:
  Linux, Debian 12.
- Siesta (development version)
  5.1-MaX-42-gb6955e60a
- Uses the Sr, Ti and O file.

# Run

```shell
SIESTA_PS_PATH=$(git rev-parse --show-toplevel)/static/siesta/PBE_fr_standard_04 siesta SrTiO3.fdf > RUN.out
```
