0-Neper_gen_3d.sh
1-gene_morp4_3-lognormal0.12.py

Step1：首先利用Neper（0-Neper_gen_3d.sh）产生voronoi结构的拓扑信息（包括点线面的结构信息），文件格式为.tess
Step2：利用python（1-gene_morp4_3-lognormal0.12.py）程序将step1的结构信息写入abaqus中，对于三维voronoi模型这个程序比较慢，所以使用另外一个导入ansys的更快一些。