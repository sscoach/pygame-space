import pygame
from scenes.base_scene import BaseScene
from scene_manager import SceneManager


class GameOverScene(BaseScene):
    def __init__(self):
        self.score_font = pygame.font.Font(None, 30)
        self.score = 0

    def on_begin(self, **kwargs):
        self.score = kwargs["score"]

    def on_key_down(self, key):
        if key == pygame.K_RETURN:
            SceneManager.instance.change("home")

    def on_render(self, surface):
        font = pygame.font.Font(None, 50)
        text = font.render("Press Enter to home", True, (255, 255, 0))
        text_rect = text.get_rect(center=(surface.get_width() / 2, surface.get_height() / 2))
        surface.blit(text, text_rect)

        text = self.score_font.render(f"Score: {self.score}", True, (255, 255, 0))
        text_rect = text.get_rect(center=(surface.get_width() / 2, surface.get_height() / 2 + 50))
        surface.blit(text, text_rect)


