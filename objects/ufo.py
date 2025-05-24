from objects.object import Object

class Ufo(Object):
    def __init__(self):
        super().__init__("assets/images/ufo.png")

        self.speed = 300
        self.direction_x = 1



