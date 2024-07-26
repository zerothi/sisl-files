set style data dots
set nokey
set xrange [0: 3.78135]
set yrange [-16.88122 : -3.07996]
set arrow from  0.99833, -16.88122 to  0.99833,  -3.07996 nohead
set arrow from  2.15109, -16.88122 to  2.15109,  -3.07996 nohead
set arrow from  2.55866, -16.88122 to  2.55866,  -3.07996 nohead
set xtics ("L"  0.00000,"G"  0.99833,"X"  2.15109,"K"  2.55866,"G"  3.78135)
 plot "silicon_band.dat"
