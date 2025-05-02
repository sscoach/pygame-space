import pygame

from constants import SCREEN_WIDTH


class Alien:
    should_change_direction = False

    def __init__(self):
        image = pygame.image.load("assets/images/alien1.png")
        self.scale_up_image = pygame.transform.scale(
            image,
            (image.get_width() * 2, image.get_height() * 2)
        )
        self.x = 0
        self.y = 0

        self.speed = 100
        self.direction = 1

    def update(self, delta_seconds):
        self.x = self.x + self.speed * self.direction * delta_seconds

        right = self.x + self.scale_up_image.get_width()

        if SCREEN_WIDTH <= right:
            Alien.should_change_direction = True
        if self.x <= 0:
            Alien.should_change_direction = True



    def draw(self, surface):
        surface.blit(self.scale_up_image, (self.x, self.y))
