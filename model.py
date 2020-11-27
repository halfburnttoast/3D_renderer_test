from point import *

class Model:
    def __init__(self):
        self.vertices = []
        self.segments = []
        
        # world-space position
        self.pos_x = 0
        self.pos_y = 0
        self.pos_z = 0
        
        # model-space rotation
        self.rot_x = 0
        self.rot_y = 0
        self.rot_z = 0
        
        # model-space scaling
        self.scale = 1.0
        
        print("Model created")
        
    # loaders
    def load_vertices(self, point_list):
        assert type(point_list) == list
        for point in point_list:
            self.vertices.append(Point(point[0], point[1], point[2]))
    def load_segments(self, segment_list):
        for segment in segment_list:
            self.segments.append(segment)
            
    # model positioning 
    def set_pos(self, x, y, z):
        self.pos_x = x
        self.pos_y = y
        self.pos_z = z
    def set_pos_delta(self, x, y, z):
        self.pos_x = self.pos_x + x
        self.pos_y = self.pos_y + y
        self.pos_z = self.pos_z + z
    def set_rot(self, x, y, z):
        self.rot_x = x
        self.rot_y = y
        self.rot_z = z
    def set_rot_delta(self, p, y, r):
        self.rot_x = (self.rot_x + p) % 360
        self.rot_y = (self.rot_y + y) % 360
        self.rot_z = (self.rot_z + r) % 360
        
    # renders the model and returns a list of the segment coordinate pairs
    def process(self, camera, fov):
        temp = list()
        out_coords = list()
        
        # the rendering stack
        for p in self.vertices:
            
            # reset point buffer
            p.clear_buffer()
            
            # do model-space rotation
            p.rot_x(self.rot_x)
            p.rot_y(self.rot_y)
            p.rot_z(self.rot_z)
            
            # do model-space scaling
            p.scale(self.scale)
            
            # place model in world-space
            p.pos(self.pos_x, self.pos_y, self.pos_z)
            
            # offset by camera world-space position
            p.pos(camera.pos_x, camera.pos_y, camera.pos_z)
            
            # rotate by camera angle
            p.rot_y(camera.angle)
            
            # perspective transform relative to camera
            p.proj(fov, 0)
            
            # retrieve tranformed points from buffer
            temp.append(p.get_buffer())
            
        # this outputs the segment point parings so that they can be passed to the grapher
        for s in self.segments:
            s1 = s[0]
            s2 = s[1]
            out_coords.append(
                [
                    #    x            y            z
                    [temp[s1][0], temp[s1][1], temp[s1][2]],  # seg point begin
                    [temp[s2][0], temp[s2][1], temp[s2][2]]  # seg point end
                ]
            )
        return out_coords
        
    # debug
    def show_vs(self):
        print("Vertices: ")
        for index, point in enumerate(self.vertices):
            print(str(index) + ":\n " + str(point.point))
        print("Segments: ")
        for index, segment in enumerate(self.segments):
            print(str(index) + ": " + str(segment))
