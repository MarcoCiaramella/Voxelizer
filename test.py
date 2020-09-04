from mesh import Mesh
from PIL import Image
from images import ImagesManager



"""img_front = "test\\front.png"
img_right = "test\\right.png"
img_left = "test\\left.png"
img_top = "test\\top.png"
img_bottom = "test\\bottom.png"
img_back = "test\\back.png"
"""

img_front = "test\\front.png"
img_right = "test\\right.png"
img_top = "test\\top.png"
img_left = img_right
img_bottom = img_top
img_back = img_front

mesh = Mesh(ImagesManager(img_front,img_back,img_right,img_left,img_top,img_bottom))
mesh.export_ply()
