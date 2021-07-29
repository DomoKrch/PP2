import pygame
import random

# CLASSES
class Obj(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

class Fall(Obj):
    
    def update(self):
        self.rect.y += 1

        if self.rect.y >= 705:
            self.rect.y = -15
            self.rect.x = random.randrange(10, w_wid - 10)

class Rise(Obj):
    def update(self):
        self.rect.y -= 1
        
        if self.rect.y <= -5:
            self.rect.y = 705
            self.rect.x = random.randrange(10, w_wid - 10)
pygame.init()

# SIZES AND COORDINATES
w_len = 700
w_wid = 600

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# GAME LOGIC
running = True
score = 0
fall_list = pygame.sprite.Group()
rise_list = pygame.sprite.Group()
obj_list = pygame.sprite.Group()
text = pygame.font.SysFont("timesnewroman", 35)

for i in range(40):
    fall = Fall(RED, 15, 15)

    fall.rect.x = random.randrange(10, w_wid - 10)
    fall.rect.y = random.randrange(10, w_len - 10)

    fall_list.add(fall)
    obj_list.add(fall)

for i in range(25):
    rise = Rise(GREEN, 15, 15)

    rise.rect.x = random.randrange(10, w_wid - 10)
    rise.rect.y = random.randrange(10, w_len - 10)

    rise_list.add(rise)
    obj_list.add(rise)

player = Obj(BLUE, 15, 15)
player.rect.x = 300
player.rect.y = 350
obj_list.add(player)

# FPS
clock = pygame.time.Clock()
fps = 30

# WINDOW SURFACE
disp = pygame.display.set_mode((w_wid, w_len))
pygame.display.set_caption("Lion Project")


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.rect.y -= 10
            if event.key == pygame.K_DOWN:
                player.rect.y += 10
            if event.key == pygame.K_LEFT:
                player.rect.x -= 10
            if event.key == pygame.K_RIGHT:
                player.rect.x += 10

    disp.fill(WHITE)

    obj_list.update()

    fall_eat_list = pygame.sprite.spritecollide(player, fall_list, True)
    rise_eat_list = pygame.sprite.spritecollide(player, rise_list, True)

    for i in fall_eat_list:
        if score - 5 > 0:
            score -= 5
        else:
            score = 0
    
    for i in rise_eat_list:
        score += 5

    obj_list.draw(disp) 

    score_text = text.render("Score: " + f'{score}', True, BLACK)
    text_pos = score_text.get_rect(center=(300, 30))
    disp.blit(score_text, text_pos)

    clock.tick(fps)
    pygame.display.flip()

pygame.quit()
