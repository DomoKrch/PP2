import pygame
import random
import json
pygame.init()

# COLORS
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# OBSTACLES
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

# SIZES AND COORDINATES
w_len = 700
w_wid = 600
x = 350
y = 300
x_food = 0
y_food = 0

# FPS
clock = pygame.time.Clock()

# SNAKE
snake = [[350, 300], [340, 300], [330, 300]]

# GAME LOGIC
running = True
food = True
direction = "down"
text = pygame.font.SysFont("timesnewroman", 60)

# FOR SAVE STATES
data = {
    "score": 0,
    "fps": 15
}

try:
    with open("save.txt", "r") as save_file:
        data = json.load(save_file)
except:
    pass

# WINDOW SURFACE
disp = pygame.display.set_mode((w_wid, w_len))
pygame.display.set_caption("Snake Project")

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT: 
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            if event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            if event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            if event.key == pygame.K_SPACE:
                with open("save.txt", "w") as save_file:
                    json.dump(data, save_file)

    disp.fill(BLACK)

    for rectan in snake:
        pygame.draw.rect(disp, GREEN, [rectan[0], rectan[1], 15, 15])

    if direction == "up":
        y -= 10
    if direction == "down":
        y += 10
    if direction == "left":
        x -= 10
    if direction == "right":
        x += 10

    snake.append([x, y])

    if food:
        x_food = random.randrange(30, w_wid - 30)
        y_food = random.randrange(30, w_len - 30)
        food = False

    pygame.draw.rect(disp, RED, (x_food, y_food, 15, 15))

    if pygame.Rect(x, y, 15, 15).colliderect(pygame.Rect(x_food, y_food, 15, 15)):
        food = True
        data["score"] += 5
        data["fps"] += 0.5
    else:
        snake.pop(0)
    
    if x >= w_wid or x <= 0:
        running = False
    if y >= w_len or y <= 0:
        running = False

    score_text = text.render("Score: " + f'{data["score"]}', True, WHITE)
    text_pos = score_text.get_rect(center=(300, 30))
    disp.blit(score_text, text_pos)
    
    clock.tick(data["fps"])
    pygame.display.flip()

pygame.quit()

