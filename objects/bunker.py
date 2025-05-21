import pygame

from objects.object import Object


class Bunker(Object):
    def __init__(self):
        super().__init__("assets/images/bunker.png")

        self.hp = 10

    def hit(self, obj):
        self.hp -= 1

    def draw(self, surface):
        others = 255 - int((10 - self.hp) * (255 / 10))
        print(f"others: {others}")
        color = (255, others, others, 255)
        print(f'color {color}')
        colored_image = self.image.copy()

        colored_image.fill(color, special_flags=pygame.BLEND_RGBA_MULT)
        surface.blit(colored_image, (self.x, self.y))
