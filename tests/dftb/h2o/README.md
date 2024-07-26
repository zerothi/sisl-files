# h2o

Simple test running DFTB+ with an H2O molecule.

- OS:
  Linux, Debian 12.
- DFTB+ 24.1
- Additional files:
  
  It uses the mio/mio-1-1 SLAKO files for O and H.

# Run

```shell
dftb+
```

Since this test is to extract a Hamiltonian and
Overlap matrix, the program will actually crash
before completing.
This is intended behaviour from DFTB+ (AFAIK).
