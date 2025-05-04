from objects.object import Object

class Beam(Object):
    def __init__(self, x, y):
        super().__init__("assets/images/beam.png")
        self.x = x
        self.y = y

        self.speed = 600
        self.direction_y = -1

