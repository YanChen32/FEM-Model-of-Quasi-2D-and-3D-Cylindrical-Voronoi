#!/bin/bash

NEPER="neper --rcfile none"

$NEPER -T -n 350 -domain "cylinder(1.,1.,30)" \
		-morpho "diameq:dirac(1),1-sphericity:lognormal(0.11,0.03)" -o gene_morp_3  -format obj

#C="-datacellcol id -datacelltrs 0.5 -cameraangle 12 -imagesize 600:600"
#$NEPER -V gene_morp_3.obj $C -showedge "cyl==0" -cameraangle 11 -print gene_morp_3

exit 0
