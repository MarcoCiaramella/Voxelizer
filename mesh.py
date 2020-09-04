from voxel import Voxel
from color import Color



class Mesh:

    PLY_HEADER_TOP = "ply\nformat ascii 1.0\nelement vertex %d\n"
    PLY_HEADER_VERTEX = "property float x\nproperty float y\nproperty float z\n"
    PLY_HEADER_NORMAL = "property float nx\nproperty float ny\nproperty float nz\n"
    PLY_HEADER_COLOR = "property uchar red\nproperty uchar green\nproperty uchar blue\n"
    PLY_HEADER_BOTTOM = "element face %d\nproperty list uchar uint vertex_indices\nend_header\n"

    def __init__(self,images_manager):
        self.images_manager = images_manager
        self.size_x = images_manager.size_x
        self.size_y = images_manager.size_y
        self.size_z = images_manager.size_z
        self.voxels = []
        self.__build()
        self.__check()

    def __build(self):
        for x in range(self.size_x):
            arr_x = []
            self.voxels.append(arr_x)
            for y in range(self.size_y):
                arr_y = []
                arr_x.append(arr_y)
                for z in range(self.size_z):
                    arr_y.append(Voxel(x,y,z))
        self.num_voxels = 0
        for x in range(self.size_x):
            for y in range(self.size_y):
                for z in range(self.size_z):
                    if self.images_manager.not_alpha(x,y,z):
                        self.voxels[x][y][z].on = True
                        self.num_voxels += 1

    def coloring(self):
        pass

    def export_ply(self):
        content = "%s%s%s%s%s"%(
            Mesh.PLY_HEADER_TOP%(self.num_voxels*Voxel.NUM_VERTICES),
            Mesh.PLY_HEADER_VERTEX,
            Mesh.PLY_HEADER_NORMAL,
            Mesh.PLY_HEADER_COLOR,
            Mesh.PLY_HEADER_BOTTOM%(self.num_voxels*Voxel.NUM_FACES)
            )
        with open('prova.ply','w') as f:
            f.write(content)
        content = ''
        for x in range(self.size_x):
            for y in range(self.size_y):
                for z in range(self.size_z):
                    if self.voxels[x][y][z].on:
                        i = 0
                        while i < Voxel.NUM_VERTICES:
                            v = i*3
                            n = i*3
                            c = i*3
                            vx = self.voxels[x][y][z].vertices[v]
                            vy = self.voxels[x][y][z].vertices[v+1]
                            vz = self.voxels[x][y][z].vertices[v+2]
                            nx = self.voxels[x][y][z].normals[n]
                            ny = self.voxels[x][y][z].normals[n+1]
                            nz = self.voxels[x][y][z].normals[n+2]
                            r = self.voxels[x][y][z].normals[c]
                            g = self.voxels[x][y][z].normals[c+1]
                            b = self.voxels[x][y][z].normals[c+2]
                            i += 1
                            content += '%f %f %f %f %f %f %d %d %d\n'%(vx,vy,vz,nx,ny,nz,r,g,b)
        with open('prova.ply','a') as f:
            f.write(content)
        content = ''
        v = 0
        for x in range(self.size_x):
            for y in range(self.size_y):
                for z in range(self.size_z):
                    if self.voxels[x][y][z].on:
                        i = 0
                        while i < Voxel.NUM_FACES:
                            i += 1
                            content += '3 %d %d %d\n'%(v,v+1,v+2)
                            v += 3
        with open('prova.ply','a') as f:
            f.write(content)

    def __check(self):
        print("num voxels "+str(self.num_voxels))
