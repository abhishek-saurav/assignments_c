import pygame

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Add Elements to My Screen")

x, y = 240, 190
width, height = 30, 30
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        x -= 3
    if pressed[pygame.K_RIGHT]:
        x += 3
    if pressed[pygame.K_UP]:
        y -= 3
    if pressed[pygame.K_DOWN]:
        y += 3

    x = min(max(0, x), 500 - width)
    y = min(max(0, y), 400 - height)

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))
    pygame.draw.circle(screen, (0, 200, 0), (400, 100), 40)
    pygame.draw.circle(screen, (0, 200, 0), (100, 300), 40, 3)
    pygame.draw.rect(screen, (255, 165, 0), pygame.Rect(x, y, width, height))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
