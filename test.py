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


x,y,z = getSize(img_front,img_right)
mesh = Mesh(x,y,z)
mesh.print()
mesh.export_ply()
