# H-chain with vibra for calculating dynamical matrices

- OS:
  Linux, Debian 12.
- Siesta (development version)
  5.1-MaX-42-gb6955e60a
- Uses the H pseudo.

# Run

```shell
SIESTA_PS_PATH=$(git rev-parse --show-toplevel)/static/siesta/PBE_sr_standard_05 siesta h_chain_fc.fdf > RUN.out
vibra h_chain_vibra.fdf > vibra.out
```
