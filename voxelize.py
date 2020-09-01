import sys
import os
from PIL import Image


img_front = sys.argv[1]
img_side = sys.argv[2]
img_top = sys.argv[3]
img_bottom = sys.argv[4]
img_back = sys.argv[5]


def getSize(img_front,img_side):
    with Image.open(img_front) as image:
        x,y = image.size
    with Image.open(img_side) as image:
        z,y = image.size
    return x,y,z
