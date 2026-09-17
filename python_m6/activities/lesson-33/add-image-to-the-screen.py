import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Add Image to the Screen")

background_image = pygame.image.load("background.png").convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

penguin_image = pygame.image.load("penguin.png").convert_alpha()
penguin_image = pygame.transform.scale(penguin_image, (200, 200))
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

font = pygame.font.Font(None, 36)
text = font.render("Hello World", True, pygame.Color("black"))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, penguin_rect.bottom + 30))


def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)
        pygame.display.flip()

        clock.tick(30)

    pygame.quit()


game_loop()
