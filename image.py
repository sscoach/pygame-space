import pygame

print("Startup")
pygame.init()
pygame.key.set_repeat(500, 500)
surface = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

image = pygame.image.load("assets/images/fighter.png")
scale_up_image = pygame.transform.scale(
    image,
    (image.get_width() * 10, image.get_height() * 10)
)

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
    surface.blit(scale_up_image, (100, 200))
    pygame.display.update()
    clock.tick(30)