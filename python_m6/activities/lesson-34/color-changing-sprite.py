import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Color Changing Sprite")

    colors = {
        "white": (255, 255, 255),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
    }
    current_color = colors["white"]

    x, y = 240, 240
    width, height = 20, 20
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
        y = min(max(0, y), 500 - height)

        if x <= 0 or x >= 500 - width:
            current_color = colors["red"]
        elif y <= 0 or y >= 500 - height:
            current_color = colors["blue"]
        else:
            current_color = colors["green"]

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color, pygame.Rect(x, y, width, height))
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


main()
