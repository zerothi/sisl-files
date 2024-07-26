# VASP calculations for a NO molecule

This folder contains a series of VASP calculations for a small
diatomic molecule (nitric oxide) that hosts an unpaired spin.

- OS:
  Linux, Debian 12.
- Uses the C POSCAR file
- VASP version:
  - 6.4.3
  - PAW's from same software version

Calculations are performed in three different flavors:
- unpolarized
- polarized
- spin-orbit

# Run

```shell
cat <PATH VASP PBE 6.4>/C_s/POTCAR >> POTCAR
# for polarized and unpolarized
vasp
# for spin-orbit
vasp_ncl
```
