from objects.object import Object

class Bomb(Object):
    def __init__(self, x, y):
        super().__init__("assets/images/bomb.png")
        self.x = x
        self.y = y

        self.speed = 200
        self.direction_y = 1
