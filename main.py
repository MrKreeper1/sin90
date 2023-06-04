import pygame
import math

FPS = 60
COLORS = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "RED": (255, 0, 0),
    "YELLOW": (255, 255, 0),
    "DYELLOW": (255, 186, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "LBLUE": (135, 206, 235)
}
WIDTH, HEIGHT = 800, 800

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sin 90 = ?")
pygame.display.set_icon(pygame.image.load("img/icon.bmp"))

clock = pygame.time.Clock()

DEG = 90
RADIUS = 250
STEP = 1

f1 = pygame.font.Font("./res/segoeuibold.ttf", 24)


class UCircle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./img/ucircle1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    def update(self):
        pass

class ALeft(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./img/aleft.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 - 64, HEIGHT - 75)
    def update(self):
        pass

class ARight(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./img/aright.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 + 64, HEIGHT - 75)
    def update(self):
        pass

class SLeft(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./img/aleft.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 - 150, HEIGHT - 75)
        self.rect.width, self.rect.height = self.rect.width // 2, self.rect.height // 2
    def update(self):
        pass

class SRight(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./img/aright.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 + 150, HEIGHT - 75)
        self.rect.width, self.rect.height = self.rect.width // 2, self.rect.height // 2
    def update(self):
        pass

running = True

all_sprites = pygame.sprite.Group()
ucircle = UCircle()
aleft, aright = ALeft(), ARight()
sleft, sright = SLeft(), SRight()
all_sprites.add(ucircle)
all_sprites.add(aleft)
all_sprites.add(aright)
all_sprites.add(sleft)
all_sprites.add(sright)

l, r = False, False


while running:
    clock.tick(FPS)
    #Ввод
    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if aleft.rect.collidepoint(event.pos):
                l = True
            if aright.rect.collidepoint(event.pos):
                r = True
            if sleft.rect.collidepoint(event.pos):
                DEG += 1
            if sright.rect.collidepoint(event.pos):
                DEG -= 1
        elif event.type == pygame.MOUSEBUTTONUP:
            l, r = False, False
        #print(event)
    if l:
        DEG += STEP
    if r:
        DEG -= STEP
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
    pygame.draw.circle(screen, COLORS["BLACK"], (WIDTH / 2, HEIGHT / 2), 3)
    #Радиус
    pygame.draw.line(screen, COLORS["RED"], (WIDTH / 2, HEIGHT / 2), (WIDTH / 2 + x, HEIGHT / 2 + y), 3)
    pygame.draw.circle(screen, COLORS["RED"], (WIDTH / 2 + x, HEIGHT / 2 + y), 5)
    #Абсцисса
    pygame.draw.line(screen, COLORS["YELLOW"], (WIDTH / 2, HEIGHT / 2), (WIDTH / 2 + x, HEIGHT / 2), 3)
    #Ордината
    pygame.draw.line(screen, COLORS["LBLUE"], (WIDTH / 2 + x, HEIGHT / 2), (WIDTH / 2 + x, HEIGHT / 2 + y), 3)
    pygame.draw.circle(screen, COLORS["LBLUE"], (WIDTH / 2 + x, HEIGHT / 2), 5)
    #Дуга
    pygame.draw.arc(screen, COLORS["DYELLOW"],
                    (WIDTH / 2 - 30, HEIGHT / 2 - 30, 60, 60),
                    0, math.radians(DEG - 90), 3)
    #Текст
    text1 = f1.render(f'Текущий угол: {DEG - 90}°', True,
                  (180, 0, 0))
    screen.blit(text1, (25, 20))
    text2 = f1.render(f'Синус: {round(math.sin(math.radians(DEG - 90)), 5)}', True,
                  COLORS["LBLUE"])
    screen.blit(text2, (25, 80))
    text3 = f1.render(f'Косинус: {round(math.cos(math.radians(DEG - 90)), 5)}', True,
                  COLORS["DYELLOW"])
    screen.blit(text3, (25, 130))
    pygame.display.flip()
    
pygame.quit()
