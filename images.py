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
        self.__check(front,back,right,left,top,bottom)

    def __get_size(self,front,right):
        with Image.open(front) as image:
            x,y = image.size
        with Image.open(right) as image:
            z,y = image.size
        return x,y,z

    def not_alpha2(self,x,y,z):
        if self.pixels_front[x,y][Color.A] == 0:
            return False
        if self.pixels_back[self.size_x-1-x,y][Color.A] == 0:
            return False
        if self.pixels_right[z,y][Color.A] == 0:
            return False
        if self.pixels_left[self.size_z-1-z,y][Color.A] == 0:
            return False
        if self.pixels_top[x,z][Color.A] == 0:
            return False
        if self.pixels_bottom[x,self.size_z-1-z][Color.A] == 0:
            return False
        return True

    def not_alpha(self,x,y,z):
        if self.pixels_front[x,y][Color.A] == 0:
            return False
        if self.pixels_back[x,y][Color.A] == 0:
            return False
        if self.pixels_right[z,y][Color.A] == 0:
            return False
        if self.pixels_left[z,y][Color.A] == 0:
            return False
        if self.pixels_top[x,z][Color.A] == 0:
            return False
        if self.pixels_bottom[x,z][Color.A] == 0:
            return False
        return True

    def __check(self,front,back,right,left,top,bottom):
        with Image.open(front) as image:
            self.__print_pixels(self.pixels_front,image.size)
        with Image.open(back) as image:
            self.__print_pixels(self.pixels_back,image.size)
        with Image.open(right) as image:
            self.__print_pixels(self.pixels_right,image.size)
        with Image.open(left) as image:
            self.__print_pixels(self.pixels_left,image.size)
        with Image.open(top) as image:
            self.__print_pixels(self.pixels_top,image.size)
        with Image.open(bottom) as image:
            self.__print_pixels(self.pixels_bottom,image.size)
        print(self.size_x,self.size_y,self.size_z)

    def __print_pixels(self,pixels,size):
        for x in range(size[0]):
                for y in range(size[1]):
                    print("pixel "+str(pixels[x,y]))
