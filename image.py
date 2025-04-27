import pygame

print("Startup")
pygame.init()
pygame.key.set_repeat(500, 500)
surface = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

image = pygame.image.load("assets/images/fighter.png")
scale_up_image = pygame.transform.scale(
    image,
    (image.get_width() * 2, image.get_height() * 2)
)
x = 640 / 2 - scale_up_image.get_width() / 2
y = 480 - scale_up_image.get_height() - 10

alien_image = pygame.image.load("assets/images/alien1.png")
scale_up_alien_image = pygame.transform.scale(
    alien_image,
    (alien_image.get_width() * 2, alien_image.get_height() * 2)
)

alien_pos = [
    (70, 100), (70 + 50, 100), (70 + 100, 100), (70 + 150, 100),
    (70, 100 + 70), (70 + 50, 100 + 70), (70 + 100, 100 + 70), (70 + 150, 100 + 70),
    (70, 100 + 70 * 2), (70 + 50, 100 + 70 * 2), (70 + 100, 100 + 70 * 2), (70 + 150, 100 + 70 * 2),
]

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
    surface.blit(scale_up_image, (x, y))

    for pos in alien_pos:
        surface.blit(scale_up_alien_image, pos)

    pygame.display.update()
    clock.tick(30)
