import pygame
from scenes.base_scene import BaseScene
from scene_manager import SceneManager


class HomeScene(BaseScene):

    def on_key_down(self, key):
        if key == pygame.K_RETURN:
            SceneManager.instance.change("game")

    def on_render(self, surface):
        font = pygame.font.Font(None, 50)
        text = font.render("Press Enter to start", True, (255, 0, 0))
        text_rect = text.get_rect(center=(surface.get_width() / 2, surface.get_height() / 2))
        surface.blit(text, text_rect)
