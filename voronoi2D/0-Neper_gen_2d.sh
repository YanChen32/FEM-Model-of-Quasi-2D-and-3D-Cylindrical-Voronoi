#!/bin/bash

NEPER="neper --rcfile none"

$NEPER -T -n 83 -dim 2 -domain "circle(1.0)" \
		-morpho "diameq:dirac(1),1-sphericity:lognormal(0.08,0.01)" -o gene_morp_3 # -format obj

#$NEPER -T -n 120 -dim 2 -domain "circle(1.)" -o gene_morp_3

#C="-datacellcol id -datacelltrs 0.5 -cameraangle 12 -imagesize 600:600"
#$NEPER -V gene_morp_3.obj $C -showedge "cyl==0" -cameraangle 11 -print gene_morp_3

exit 0

