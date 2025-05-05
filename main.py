import pygame

from objects.alien import Alien
from objects.fighter import Fighter
from objects.beam import Beam

from constants import *

print("Startup")
pygame.init()
pygame.key.set_repeat(100, 100)
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

fighter = Fighter()
beam = None

aliens = []
for y in range(2):  # y: 0, 1
    for x in range(3):  # x: 0, 1, 2
        alien = Alien()
        aliens.append(alien)
        alien.x = 70 + 50 * x
        alien.y = 100 + 70 * y

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
            if event.key == pygame.K_LEFT:
                fighter.direction_x = -1
            if event.key == pygame.K_RIGHT:
                fighter.direction_x = +1
            if event.key == pygame.K_SPACE:
                if beam is None:
                    beam = Beam(fighter.x + fighter.image.get_width()/2, fighter.y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter.direction_x = 0
            if event.key == pygame.K_RIGHT:
                fighter.direction_x = 0

    delta_seconds = clock.tick(FPS) / 1000
    fighter.update(delta_seconds)
    if beam:
        beam.update(delta_seconds)
        if beam.y < 0:
            beam = None

    for alien in aliens:
        alien.update(delta_seconds)

    if Alien.should_change_direction:
        Alien.should_change_direction = False

        for alien in aliens:
            alien.direction_x *= -1
            alien.move(0, 50)

    # print("Render")
    surface.fill((0, 0, 0))
    fighter.draw(surface)
    if beam:
        beam.draw(surface)

    for alien in aliens:
        alien.draw(surface)

    pygame.display.update()


