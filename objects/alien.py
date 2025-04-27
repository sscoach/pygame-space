import pygame


class Alien:
    def __init__(self):
        image = pygame.image.load("assets/images/alien1.png")
        self.scale_up_image = pygame.transform.scale(
            image,
            (image.get_width() * 2, image.get_height() * 2)
        )
        self.x = 0
        self.y = 0

    def draw(self, surface):
        surface.blit(self.scale_up_image, (self.x, self.y))
