from objects.object import Object

class Bunker(Object):
    def __init__(self, x, y):
        super().__init__("assets/images/bunker.png")

        self.x = x
        self.y = y

        self.hp = 10