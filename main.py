import pygame

from objects.alien import Alien
from objects.fighter import Fighter

from constants import *

print("Startup")
pygame.init()
pygame.key.set_repeat(500, 500)
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

fighter = Fighter()

aliens = []
for y in range(2):  # y: 0, 1
    for x in range(3):  # x: 0, 1, 2
        alien = Alien()
        aliens.append(alien)
        alien.x = 70 + 50 * x
        alien.y = 100 + 70 * y

while True:

    print("Update")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Shutdown")
            pygame.quit()
            exit()
            break

    print("Render")
    surface.fill((0, 0, 0))
    fighter.draw(surface)

    for alien in aliens:
        alien.draw(surface)

    pygame.display.update()
    clock.tick(FPS)

