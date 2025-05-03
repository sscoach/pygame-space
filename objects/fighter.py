from constants import *
from objects.object import Object


class Fighter(Object):
    def __init__(self):
        super().__init__("assets/images/fighter.png")

        self.x = SCREEN_WIDTH / 2 - self.image.get_width() / 2
        self.y = SCREEN_HEIGHT - self.image.get_height() - 10
