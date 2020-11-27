import numpy

# Point system. Handles transformations.
# Stores two points:
#   self.point : the original point 
#   self.buffer: the temporary point used as an output for transformations
# When the point is created, it's given a x, y, z coordinate that shouldn't be changed
# beause it's part of the model's local space. When it comes time to render the model
# the buffer is loaded with the original point by calling clear_buffer(). From that point
# the user can call various transformations below that act on the buffer. When the 
# transformations are complete, the user calls get_buffer(), which returns a tuple with
# the data from the buffer. The model module then sends these results to the grapher to
# be rendered on the screen.
class Point:
    def __init__(self, x, y, z):
        self.point = numpy.matrix(
            [
                [x],
                [y],
                [z]
            ]
        )
        self.buffer = numpy.matrix(
            [
                [0],
                [0],
                [0]
            ]
        )

    # reset the buffer, this should be the first function to be called by the render stack!
    def clear_buffer(self):
        self.buffer = numpy.matrix(self.point)
        
    # returns a tuple containing the results from the transformations
    def get_buffer(self):
        o = self.buffer.tolist()
        return (
            o[0][0],
            o[1][0],
            o[2][0]
        )
        
    # rotation transformations
    def rot_x(self, angle):
        angle = numpy.deg2rad(angle)
        rot = numpy.matrix(
            [
                [1, 0, 0],
                [0, numpy.cos(angle), -numpy.sin(angle)],
                [0, numpy.sin(angle), numpy.cos(angle)]
            ]
        )
        self.buffer = rot * self.buffer 
    def rot_y(self, angle):
        angle = numpy.deg2rad(angle)
        rot = numpy.matrix(
            [
                [numpy.cos(angle), 0, numpy.sin(angle)],
                [0, 1, 0],
                [-numpy.sin(angle), 0, numpy.cos(angle)]
            ]
        )
        self.buffer = rot * self.buffer
    def rot_z(self, angle):
        angle = numpy.deg2rad(angle)
        rot = numpy.matrix(
            [
                [numpy.cos(angle), -numpy.sin(angle), 0],
                [numpy.sin(angle), numpy.cos(angle), 0],
                [0, 0, 1]
            ]
        )
        self.buffer = rot * self.buffer
        
    # scale transformation
    def scale(self, factor):
        self.buffer = factor * self.buffer
    
    # transposition transformations
    def pos(self, x, y, z):
        pos = numpy.matrix(
            [
                [x],
                [y],
                [z]
            ]
        )
        self.buffer = pos + self.buffer
            
    # a "fake" perspective projection. AKA: doesn't handle aspect ratios.
    # set dist to 0 to go first-person. if dist > 0, rotations become 3rd person
    def proj(self, fov = 70, dist = 0):
        """For first person, dist should be set to 0"""
        f = fov / (dist + self.buffer.tolist()[2][0])
        p = numpy.matrix(
            [
                [f, 0, 0],
                [0, -f, 0],
                [0, 0, 1]
            ]
        )
        self.buffer = p * self.buffer
