# Fe bcc iron

Simple test running iron bcc.
It creates bands.

- OS:
  Linux, Debian 12.
- Siesta (development version)
  5.1-MaX-12-g8bcc883a9
- Uses the Fe.psml input file.

# Run

```shell
SIESTA_PS_PATH=$(git rev-parse --show-toplevel)/static/siesta/PBE_sr_standard_05 siesta fe.fdf > run.out
```
