set cbrange [-1:1]
unset ztics 
set border lw 3
set palette defined (-1 "blue", -0.1 "gray", 0 "white", 0.1 "gray", 1 "red")
set grid xtics lw 3 lt 1 lc "black"
set xtics ("-Y" 15, "{/Symbol G}" 51, "Y" 86.4) 
set xtics font "Helvetica,24"
set ytics font "Helvetica,18" 
set xtics offset 0,-0.5
set ytics offset 0,0
set grid front 
f(z)=z**(0.7) 
ef=11.3 
set xra[15:86.5]
Emin = 0.0-ef
Emax = 20.005-ef
set yra[-5:0]
unset ztics 
unset key 
#
set pm3d
set view 0,0
splot './sommati_wfc4_sigma_YGY' u 1:($2 - ef):($4) w pm3d 

