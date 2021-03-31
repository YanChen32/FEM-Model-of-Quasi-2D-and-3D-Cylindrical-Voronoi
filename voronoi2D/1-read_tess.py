from abaqus import *
from abaqusConstants import *
import os
import math
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()

def ReadTess(file_header):
	# Open the .tess file, and read all the lines. Store only the contents of the sections named
	# **vertex **edge  and **face for further parsing of the system.
	
	# Open the file
	with open(file_header + '.tess') as file:
		content = file.read().splitlines()
	
	# Initialize data saving arrays
	vertex=[]
	edge=[]
	face=[]
	vertex_flag = 0
	edge_flag = 0
	face_flag = 0
	
	# Strip only the CELL and COORD sections
	for line in range (0, len(content)):
		content_line = content[line].lstrip()
		if content_line == '**vertex':
			vertex_flag = 1
		if content_line == '**edge':
			vertex_flag = 0
			edge_flag = 1
		if content_line == '**face':
			edge_flag = 0
			face_flag = 1
		if content_line == '**polyhedron':
			face_flag = 0
			
		# Strip only the vertex, edge, and face sections	
		if vertex_flag == 1:
			vertex.append(content_line)
		if edge_flag == 1:
			edge.append(content_line)
		if face_flag == 1:
			face.append(content_line)		
	# Return the information	
	return (vertex, edge, face)

#def Line_inverse(line):

file_name = 'gene_morp_3'
vertex, edge, face=ReadTess(file_name)

Num_vertex = int(vertex[1])
Num_edge = int(edge[1])
Num_face = int(face[1])
del vertex[0:2]
del edge[0:2]
del face[0:2]

#for item in vertex: print(item)

p = mdb.Model(name='Voroitria2D')
mySketch=p.ConstrainedSketch(name='Voroitria2D',sheetSize=1.0)

#myModel=mdb.Model(name='Voroitria')
#mySketch=myModel.ConstrainedSketch(name='Voroitria',sheetSize=2000.0)


lenX = 0.1
lenY = 0.1
lenZ = 0.1

# ------------------------------------------------------ #
# plot all edges
# note that, mid-points for all edges should be saved
# edges can be conviently indexed by: p.edges.findAt((X, Y, Z))
# ------------------------------------------------------ #

# for item in p.edges:print(item)
for eLine in edge:
	n_v1 = int(eLine.split()[1]) # index for 1st vertex
	n_v2 = int(eLine.split()[2]) # index for 2nd vertex
	vertex1 = vertex[n_v1-1].split()[1:4]
	vertex2 = vertex[n_v2-1].split()[1:4]
	point1_x = lenX*float(vertex1[0])
	point1_y = lenY*float(vertex1[1])
	point1_z = lenZ*float(vertex1[2])
	point2_x = lenX*float(vertex2[0])
	point2_y = lenY*float(vertex2[1])
	point2_z = lenZ*float(vertex2[2])
	#if abs(point1_z - lenZ)<1e-4 and abs(point2_z - lenZ)< 1e-4:
	mySketch.Line((point1_x,point1_y),(point2_x,point2_y))



