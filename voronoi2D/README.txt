0-Neper_gen_2d.sh
1-read_tess.py

Step1：首先利用Neper（0-Neper_gen_2d.sh）产生voronoi结构的拓扑信息（包括点线面的结构信息），文件格式为.tess
Step2：利用python（1-read_tess.py）程序将step1的结构信息写入abaqus中