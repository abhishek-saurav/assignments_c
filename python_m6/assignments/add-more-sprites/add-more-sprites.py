import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 60

pygame.init()

background_image = pygame.transform.scale(
    pygame.image.load("pet_bg.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT)
)

font = pygame.font.SysFont("Arial", FONT_SIZE)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Add More Sprites")

all_sprites = pygame.sprite.Group()
food_group = pygame.sprite.Group()

pet = Sprite(pygame.Color("brown"), 40, 40)
pet.rect.x = 30
pet.rect.y = 180
all_sprites.add(pet)

num_food_items = 4
for _ in range(num_food_items):
    food = Sprite(pygame.Color("orange"), 30, 30)
    food.rect.x = random.randint(100, SCREEN_WIDTH - food.rect.width)
    food.rect.y = random.randint(0, SCREEN_HEIGHT - food.rect.height)
    food_group.add(food)
    all_sprites.add(food)

score = 0
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
    y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
    pet.move(x_change, y_change)

    for food in list(food_group):
        if pet.rect.colliderect(food.rect):
            food_group.remove(food)
            all_sprites.remove(food)
            score += 1

    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    score_text = font.render(str(score), True, pygame.Color("black"))
    screen.blit(score_text, (10, 10))

    if score == num_food_items:
        win_text = font.render("All Food Collected!", True, pygame.Color("black"))
        text_x = (SCREEN_WIDTH - win_text.get_width()) // 2
        text_y = (SCREEN_HEIGHT - win_text.get_height()) // 2
        screen.blit(win_text, (text_x, text_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
