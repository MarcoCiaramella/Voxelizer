from vector3f import Vector3f


class Voxel:

    NUM_VERTICES = 36
    NUM_FACES = 12

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.position = Vector3f(x+0.5,y+0.5,z+0.5)
        self.__init_vertices()
        self.__init_indices()
        self.__init_normals()
        self.__init_colors()
        self.on = False

    def __init_vertices(self):
        min_x = self.x
        max_x = self.x+1
        min_y = self.y
        max_y = self.y+1
        min_z = self.z
        max_z = self.z-1
        face_front = [
            min_x,min_y,max_z,
            max_x,min_y,max_z,
            max_x,max_y,max_z,
            max_x,max_y,max_z,
            min_x,max_y,max_z,
            min_x,min_y,max_z
            ]
        face_right = [
            max_x,min_y,max_z,
            max_x,min_y,min_z,
            max_x,max_y,min_z,
            max_x,max_y,min_z,
            max_x,max_y,max_z,
            max_x,min_y,max_z
            ]
        face_back = [
            min_x,max_y,min_z,
            max_x,max_y,min_z,
            max_x,min_y,min_z,
            max_x,min_y,min_z,
            min_x,min_y,min_z,
            min_x,max_y,min_z
            ]
        face_left = [
            min_x,min_y,min_z,
            min_x,min_y,max_z,
            min_x,max_y,max_z,
            min_x,max_y,max_z,
            min_x,max_y,min_z,
            min_x,min_y,min_z
            ]
        face_bottom = [
            min_x,min_y,min_z,
            max_x,min_y,min_z,
            max_x,min_y,max_z,
            max_x,min_y,max_z,
            min_x,min_y,max_z,
            min_x,min_y,min_z
            ]
        face_top = [
            min_x,max_y,max_z,
            max_x,max_y,max_z,
            max_x,max_y,min_z,
            max_x,max_y,min_z,
            min_x,max_y,min_z,
            min_x,max_y,max_z
            ]
        self.vertices = face_front + face_right + face_back + face_left + face_bottom + face_top

    def __init_indices(self):
        self.indices = [
            0,1,2,
            3,4,5,
            6,7,8,
            9,10,11,
            12,13,14,
            15,16,17,
            18,19,20,
            21,22,23,
            24,25,26,
            27,28,29,
            30,31,32,
            33,34,35
            ]

    def __init_normals(self):
        self.normals = [
            0,0,1,
            0,0,1,
            0,0,1,
            0,0,1,
            0,0,1,
            0,0,1,
            1,0,0,
            1,0,0,
            1,0,0,
            1,0,0,
            1,0,0,
            1,0,0,
            0,0,-1,
            0,0,-1,
            0,0,-1,
            0,0,-1,
            0,0,-1,
            0,0,-1,
            -1,0,0,
            -1,0,0,
            -1,0,0,
            -1,0,0,
            -1,0,0,
            -1,0,0,
            0,-1,0,
            0,-1,0,
            0,-1,0,
            0,-1,0,
            0,-1,0,
            0,-1,0,
            0,1,0,
            0,1,0,
            0,1,0,
            0,1,0,
            0,1,0,
            0,1,0
            ]

    def __init_colors(self):
        self.colors = [
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0
        ]

    def coloring(self,colors):
        color_front = self.__get_face_color(colors['front'])
        color_back = self.__get_face_color(colors['back'])
        color_right = self.__get_face_color(colors['right'])
        color_left = self.__get_face_color(colors['left'])
        color_top = self.__get_face_color(colors['top'])
        color_bottom = self.__get_face_color(colors['bottom'])
        self.colors = []
        self.colors = color_front + color_right + color_back + color_left + color_bottom + color_top

    def __get_face_color(self,color):
        return color+color+color+color+color+color