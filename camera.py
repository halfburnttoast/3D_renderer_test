# Camera class. 

class Camera:
    def __init__(self):
        self.angle = 0.0
        self.pos_x = 0.0
        self.pos_y = 5
        self.pos_z = 0.0
        self.move_rate = 0.2
        self.rot_rate = 0.8
        
        print("Camera created")
    def reset(self):
        self.angle = 0.0
        self.pos_x = 0.0
        self.pos_y = 0.0
        self.pos_z = 0.0       
