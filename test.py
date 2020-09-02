from mesh import Mesh
from PIL import Image



img_front = "test\\front.png"
img_right = "test\\right.png"
img_left = "test\\left.png"
img_top = "test\\top.png"
img_bottom = "test\\bottom.png"
img_back = "test\\back.png"

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
