from constants import SCREEN_WIDTH
from objects.object import Object


class Alien(Object):
    should_change_direction = False

    def __init__(self):
        super().__init__("assets/images/alien1.png")

        self.speed = 100
        self.direction = 1

    def update(self, delta_seconds):
        super().update(delta_seconds)

        right = self.x + self.image.get_width()

        if SCREEN_WIDTH <= right:
            Alien.should_change_direction = True
        if self.x <= 0:
            Alien.should_change_direction = True
