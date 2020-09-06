import sys
import os
from PIL import Image
from mesh import Mesh
from images import ImagesManager



if len(sys.argv) != 8:
    print("Usage: python voxelize.py <img front> <img right> <img left> <img top> <img bottom> <img back> <ply output file>")
    exit()

img_front = sys.argv[1]
img_right = sys.argv[2]
img_left = sys.argv[3]
img_top = sys.argv[4]
img_bottom = sys.argv[5]
img_back = sys.argv[6]
ply = sys.argv[7]
if ply[-4:] != '.ply':
    ply += '.ply'

mesh = Mesh(ImagesManager(img_front,img_back,img_right,img_left,img_top,img_bottom))
mesh.export_ply(ply)

print('output: '+ply)
