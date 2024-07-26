# Bi 2D hexagonal structure

Topological insulator Bismuth 2D hexagonal
lattice.

Each sub-lattice is offset by 1.62 Ang.

- OS:
  Linux, Debian 12.
- Siesta (development version)
  5.1-MaX-12-g8bcc883a9
- Uses the Bi.psml file.

# Run

```shell
SIESTA_PS_PATH=$(git rev-parse --show-toplevel)/static/siesta/PBE_fr_standard_04 siesta Bi_hexagonal.fdf > RUN.out
```
