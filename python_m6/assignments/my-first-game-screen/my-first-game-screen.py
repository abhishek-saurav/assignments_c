import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Game Screen")

font = pygame.font.Font(None, 40)
title_text = font.render("Abhishek's Game Screen", True, pygame.Color("white"))
title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color("darkblue"))
    screen.blit(title_text, title_rect)
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
