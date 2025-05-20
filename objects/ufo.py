from objects.object import Object


class Ufo(Object):
    def __init__(self):
        super().__init__("assets/images/ufo.png")

        self.speed = 100
        self.direction_x = 1

        self.x = 0
        self.y = 50

        self.score = 1000
        self.bonus_score = 500