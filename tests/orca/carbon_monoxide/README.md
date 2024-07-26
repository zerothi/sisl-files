# CO molecule calculation

- OS:
  Linux, Debian 12.
- ORCA (development version)
  5.0.4

These tests can currently not be used with ORCA 6, since
the tests in sisl, are using 5 formats.

Note also, that D3 has some errors in <5.0.4 releases.

# Run

```shell
$(which orca) molecule.inp > molecule.output
```
