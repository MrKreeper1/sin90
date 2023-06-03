import pygame
import math

FPS = 60
COLORS = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "RED": (255, 0, 0),
    "YELLOW": (255, 255, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "LBLUE": (135, 206, 235)
}
WIDTH, HEIGHT = 800, 800

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

DEG = 90
RADIUS = 250
STEP = 1

f1 = pygame.font.Font(None, 36)


class UCircle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./img/ucircle1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    def update(self):
        pass
running = True

all_sprites = pygame.sprite.Group()
ucircle = UCircle()
all_sprites.add(ucircle)
while running:
    clock.tick(FPS)
    #Ввод
    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        print(event)
    if keys[pygame.K_LEFT]:
        DEG += STEP
    if keys[pygame.K_RIGHT]:
        DEG -= STEP
    if DEG < 90:
        DEG = 360 + DEG
        
    #Обновление
    all_sprites.update()
    DEG = (DEG - 90) % 360 + 90
    x = math.sin(math.radians(DEG)) * RADIUS
    y = math.cos(math.radians(DEG)) * RADIUS

    #Отрисовка
    screen.fill(COLORS["WHITE"])
    all_sprites.draw(screen)
    #Оси
    pygame.draw.line(screen, COLORS["BLACK"], (WIDTH / 2 - RADIUS - 10, HEIGHT / 2), (WIDTH / 2 + RADIUS + 10, HEIGHT / 2))
    pygame.draw.line(screen, COLORS["BLACK"], (WIDTH / 2, HEIGHT / 2 + RADIUS + 10), (WIDTH / 2, HEIGHT / 2 - RADIUS - 10))
    #Радиус
    pygame.draw.line(screen, COLORS["RED"], (WIDTH / 2, HEIGHT / 2), (WIDTH / 2 + x, HEIGHT / 2 + y), 3)
    pygame.draw.circle(screen, COLORS["RED"], (WIDTH / 2 + x, HEIGHT / 2 + y), 5)
    #Абсцисса
    pygame.draw.line(screen, COLORS["YELLOW"], (WIDTH / 2, HEIGHT / 2), (WIDTH / 2 + x, HEIGHT / 2), 3)
    #Ордината
    pygame.draw.line(screen, COLORS["LBLUE"], (WIDTH / 2 + x, HEIGHT / 2), (WIDTH / 2 + x, HEIGHT / 2 + y), 3)
    #Текст
    text1 = f1.render(f'Текущий угол: {DEG - 90}°', True,
                  (180, 0, 0))
    screen.blit(text1, (25, 20))
    text2 = f1.render(f'Синус: {round(math.sin(math.radians(DEG - 90)), 5)}', True,
                  (180, 0, 0))
    screen.blit(text2, (25, 80))
    text3 = f1.render(f'Косинус: {round(math.cos(math.radians(DEG - 90)), 5)}', True,
                  (180, 0, 0))
    screen.blit(text3, (25, 130))
    pygame.display.flip()
    
pygame.quit()
