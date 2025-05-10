import pygame
from scenes.base_scene import BaseScene


class GameOverScene(BaseScene):

    def on_render(self, surface):
        font = pygame.font.Font(None, 50)
        text = font.render("Press Enter to home", True, (255, 255, 0))
        text_rect = text.get_rect(center=(surface.get_width() / 2, surface.get_height() / 2))
        surface.blit(text, text_rect)
