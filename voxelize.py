import sys
import os
from PIL import Image


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
