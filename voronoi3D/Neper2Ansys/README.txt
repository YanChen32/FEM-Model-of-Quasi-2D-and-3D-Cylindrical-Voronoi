Step 1: Generate the topological information of 3D Voronoi structure (including the points, lines and surface, etc), and the file format is Obj.
Command: bash Neper_gen_3d.sh

Step 2: Transform the Obj file of Step 1 to ANSYS APDL file, for example, gene_morp_3.txt.
Command: python 1-obj_gene_APDL_ansys.py

Step 3: gene_ morp_ 3.txt can be directly executed by ANSYS to generate the 3D geometrical structure. You can export it to .iges file, then import it into ABAQUS.

