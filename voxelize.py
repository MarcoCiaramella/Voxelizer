import sys
import os
from PIL import Image
from mesh import Mesh


img_front = sys.argv[1]
img_right = sys.argv[2]
img_left = sys.argv[3]
img_top = sys.argv[4]
img_bottom = sys.argv[5]
img_back = sys.argv[6]


def getSize(img_front,img_right):
    with Image.open(img_front) as image:
        x,y = image.size
    with Image.open(img_right) as image:
        z,y = image.size
    return x,y,z


pixels_front = Image.open(img_front).load()
pixels_back = Image.open(img_back).load()
pixels_right = Image.open(img_right).load()
pixels_left = Image.open(img_left).load()
pixels_top = Image.open(img_top).load()
pixels_bottom = Image.open(img_bottom).load()

x,y,z = getSize(img_front,img_right)
mesh = Mesh(x,y,z)
mesh.coloring(pixels_front,pixels_back,pixels_right,pixels_left,pixels_top,pixels_bottom)
mesh.export_ply()
