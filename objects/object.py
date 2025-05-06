import pygame


class Object:
    def __init__(self, image_path):
        original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(
            original_image,
            (original_image.get_width() * 2, original_image.get_height() * 2)
        )
        self.x = 0
        self.y = 0

        self.speed = 200
        self.direction_x = 0
        self.direction_y = 0

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def update(self, delta_seconds):
        self.move(self.speed * self.direction_x * delta_seconds,
                  self.speed * self.direction_y * delta_seconds)

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def check_collision(self, others):
        for other in others:
            if self.rect.colliderect(other.rect):
                return other
        return None