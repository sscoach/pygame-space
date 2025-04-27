import pygame


class Fighter:
    def __init__(self):
        image = pygame.image.load("assets/images/fighter.png")
        self.scale_up_image = pygame.transform.scale(
            image,
            (image.get_width() * 2, image.get_height() * 2)
        )
        self.x = 640 / 2 - self.scale_up_image.get_width() / 2
        self.y = 480 - self.scale_up_image.get_height() - 10

    def draw(self, surface):
        surface.blit(self.scale_up_image, (self.x, self.y))
