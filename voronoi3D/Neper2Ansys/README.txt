0-Neper_gen_3d.sh
1-obj_gene_APDL_ansys.py

Step1：首先利用Neper（0-Neper_gen_3d.sh）产生voronoi结构的拓扑信息（包括点线面的结构信息），文件格式为.obj
Step2：利用python（1-obj_gene_APDL_ansys.py）程序将step1的结构信息转化为ansys APDL的gene_morp_3.txt文件，这个gene_morp_3.txt可以直接导入Ansys，速度非常快。