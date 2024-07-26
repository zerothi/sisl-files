# MgCO3 molecular dynamics with a Nose thermostat

This is from the older 4.1 test suite.

Used for:
- testing MD output

- OS:
  Linux, Debian 12.
- Siesta (development version)
  5.1-MaX-42-gb6955e60a
- Uses the Mg, C and O pseudos.

# Run

```shell
SIESTA_PS_PATH=$(git rev-parse --show-toplevel)/static/siesta/PBE_sr_standard_05 siesta md_nose.fdf > RUN.out
```
