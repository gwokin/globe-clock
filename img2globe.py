#!/usr/bin/python

import sys
import numpy as np
import Image
import matplotlib.pyplot as plt


rmat = [[1.,0,0],[0,0,-1.],[0,1.,0]]

def gen_points(w,h,tex_map):
    points = []
    for x in range(w):
        percx = ((x+(1./w)) / w)
        lat = 2 * np.pi * percx - np.pi

        for y in range(h):
            percy = ((y+(1./h)) / h)
            lon = np.pi * percy 

            p = [np.cos(lat)*np.sin(lon), 
                 -1*np.cos(lon),
                 -1* np.sin(lat)*np.sin(lon)]

            new_p = []
            for row in rmat:
                new_p.append(np.dot(row, p))

            points.append([new_p[0], new_p[1], new_p[2], tex_map.getpixel((percx*tex_map.size[0],percy*tex_map.size[1]))])
    return points



if len(sys.argv) > 1:
    print "  using",sys.argv[1]," as tex map"
    
    tmap = Image.open(sys.argv[1])
    print "    width: ",tmap.size[0]
    print "    height:",tmap.size[1]
    
    pts = gen_points(144,72,tmap)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for x,y,z,color in pts:
        ax.scatter3D(x, y, z, c=color)
