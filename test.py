from mesh import Mesh
from PIL import Image
from images import ImagesManager



img_front = "img\\front.png"
img_right = "img\\right.png"
img_left = "img\\left.png"
img_top = "img\\top.png"
img_bottom = "img\\bottom.png"
img_back = "img\\back.png"


"""img_front = "img\\front.png"
img_back = img_front
img_right = "img\\right.png"
img_left = img_right
img_top = "img\\top.png"
img_bottom = img_top"""


mesh = Mesh(ImagesManager(img_front,img_back,img_right,img_left,img_top,img_bottom))
mesh.export_ply('test.ply')
