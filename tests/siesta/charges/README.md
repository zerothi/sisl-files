# Graphene calculations with partial charges

This is to check the output files and ensure that sisl
can parse the output files in a consistent manner.

- OS:
  Linux, Debian 12.
- Uses the C.psml input file.

This test contains several sub-folders because
it tries a varying amount of tests and combinations.
Its main test is the charge outputs by:
- Mulliken
- Voronoi
- Hirshfeld

They are printed in various environments:
- every step of MD
- every SCF step
- unpolarized
- polarized
- non-collinear

# Run

```shell
export SIESTA_PS_PATH=$(git rev-parse --show-toplevel)/static/siesta/PBE_fr_standard_04
function run_dir {
   mkdir $1
   cd $1
   siesta ../charge_$1.fdf > RUN.out
   cd ..
}
run_dir end
for d in md md_scf nc_md nc_md_scf nc_scf pol_md pol_md_scf soc_md_scf
do
  run_dir $d
done
```
