from model import Model

# model test
class Cube(Model):
    def __init__(self):
        Model.__init__(self)
        self.load_vertices([
            [-1,  1, 1],
            [ 1,  1, 1],
            [ 1, -1, 1],
            [-1, -1, 1],
            [-1,  1, -1],
            [ 1,  1, -1],
            [ 1, -1, -1],
            [-1, -1, -1]
            ])
        self.load_segments([
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0),
            (4, 5),
            (5, 6),
            (6, 7),
            (7, 4),
            (0, 4),
            (1, 5),
            (3, 7),
            (2, 6)
            ])
        self.scale = 1
