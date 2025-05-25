import pygame

from objects.object import Object

class Bunker(Object):
    def __init__(self, x, y):
        super().__init__("assets/images/bunker.png")

        self.x = x
        self.y = y

        self.hp = 10

    def make_red(self):
        step = 255/10
        color_sub = (0, step, step)
        self.image.fill(color_sub, special_flags=pygame.BLEND_SUB)