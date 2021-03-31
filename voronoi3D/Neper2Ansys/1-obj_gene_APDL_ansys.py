# ------------------------------------------------------ #
#
# generate APDL for using in Ansys
# generate 3D Voronoi model using point/line/face infos of .tess file generated by Neper
# Created: 12/29/2019
# Modified: 12/30/2019
# Author: Yan Chen, P.hd, Xi'an Jiatong University
# Email: chenyanc@stu.xjtu.edu.cn
# 
# ------------------------------------------------------ #

import os
import math

lenX = 0.1    # 2 mm
lenY = 0.1
lenZ = 0.1

file_name = 'gene_morp_3'
# write APDL file 
APDL = open(file_name+'.txt','w')  

with open(file_name + '.obj') as file:
	content = file.read().splitlines()

# Initialize data saving arrays
vertex=[]
face=[]
vertex_flag = 0
face_flag = 0

APDL.write('/prep7\n') # title
n_points=1    # point id in APDL
# Strip only the CELL and COORD sections
for line in range (0, len(content)):
	content_line = content[line].lstrip()
	data = content_line.split() 
	if data[0] == 'v':
		x,y,z = lenX*float(data[1]), lenY*float(data[2]), lenZ*float(data[3])
		APDL.write('k,{0},{1},{2},{3} \n'.format(n_points,x,y,z))
		n_points = n_points+1
	if data[0] == 'f':
		APDL.write('a,%s\n'%','.join(data[1:]))
		

APDL.close()	









	