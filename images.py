from PIL import Image
from color import Color



class ImagesManager:

    def __init__(self,front,back,right,left,top,bottom):
        self.pixels_front = Image.open(front).load()
        self.pixels_back = Image.open(back).load()
        self.pixels_right = Image.open(right).load()
        self.pixels_left = Image.open(left).load()
        self.pixels_top = Image.open(top).load()
        self.pixels_bottom = Image.open(bottom).load()
        self.size_x,self.size_y,self.size_z = self.__get_size(front,right)

    def __get_size(self,front,right):
        with Image.open(front) as image:
            x,y = image.size
        with Image.open(right) as image:
            z,y = image.size
        return x,y,z

    def not_alpha(self,x,y,z):
        if self.pixels_front[x,y][Color.A] == 0:
            return False
        if self.pixels_back[self.size_x-x,y][Color.A] == 0:
            return False
        if self.pixels_right[z,y][Color.A] == 0:
            return False
        if self.pixels_left[self.size_z-z,y][Color.A] == 0:
            return False
        if self.pixels_top[x,z][Color.A] == 0:
            return False
        if self.pixels_bottom[x,self.size_z-z][Color.A] == 0:
            return False
        return True
