from model import Model

class Wall(Model):
    def __init__(self):
        Model.__init__(self)
        self.load_vertices([
            [-2,  1, 0],
            [ 2,  1, 0],
            [ 2, -1, 0],
            [-2, -1, 0]
        ])
        self.load_segments([
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0)
        ])
