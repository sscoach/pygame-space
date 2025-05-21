import pygame

from objects.object import Object


class Bunker(Object):
    def __init__(self):
        super().__init__("assets/images/bunker.png")

        self.hp = 10

    def hit(self):
        self.hp -= 1

        self.make_red()

    def make_red(self):
        green_blue = 255 / 10
        color_sub = (0, green_blue, green_blue)
        self.image.fill(color_sub, special_flags=pygame.BLEND_SUB)
