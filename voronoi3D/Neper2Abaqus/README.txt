Step1：Create 3D voronoi structure (including structural information of point, line and surface) with .tess format using Neper code.
command: bash 0-Neper_gen_3d.sh

Step2：Import the structure information of Step 1 into ABAQUS via Python interface (1-gene_morp4_3-lognormal0.12.py).

Note that, the import process may be slow for bigger 3D voronoi structures. It's faster to use another method via interface of ANSYS.

