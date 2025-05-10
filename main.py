import pygame

from objects.alien import Alien
from objects.fighter import Fighter
from objects.beam import Beam
from objects.explosion import Explosion
from scenes.game_scene import GameScene
from scenes.home_scene import HomeScene
from scenes.game_over_scene import GameOverScene
from constants import *

print("Startup")
pygame.init()
pygame.key.set_repeat(500, 300)
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

scene = GameOverScene()
scene.on_begin()

while True:

    # print("Update")
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            print("Shutdown")
            pygame.quit()
            exit()
            break
        if event.type == pygame.KEYDOWN:
            scene.on_key_down(event.key)

        if event.type == pygame.KEYUP:
            scene.on_key_up(event.key)

    delta_seconds = clock.tick(FPS) / 1000
    scene.on_update(delta_seconds)

    # print("Render")
    surface.fill((0, 0, 0))
    scene.on_render(surface)

    pygame.display.update()


