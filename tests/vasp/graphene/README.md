# Graphene calculation

This is to check the output files and ensure that sisl
can parse the output files in a consistent manner.

- OS:
  Linux, Debian 12.
- Uses the C POSCAR file
- VASP version:
  - 6.4.3
  - PAW's from same software version

# Run

```shell
cat <PATH VASP PBE 6.4>/C_s/POTCAR >> POTCAR
vasp
```
