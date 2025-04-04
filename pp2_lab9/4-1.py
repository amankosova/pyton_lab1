import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Түстерді анықтау
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Бағдарламада қолданылатын басқа айнымалылар
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

# Шрифттерді орнату
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Фон суретін жүктеу
background = pygame.image.load("AnimatedStreet.png")

# Ақ экран жасау
screen = pygame.display.set_mode((400, 600))
screen.fill(WHITE)
pygame.display.set_caption("Racer")

# Қарсыластардың (Enemy) класы
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)  # Қарсыласты төменге жылжыту
        if (self.rect.top > 600):  # Экраннан тыс шыққан кезде жаңа орынға қайтадан пайда болады
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Монеталар (Coin) класы
c1, c2, c3, c4, c5 = False, False, False, False, False
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (40, 40))  # Монетаның өлшемін өзгерту
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))

    def move(self):
        global COINS
        global SPEED
        # Монетаның орналасуына байланысты ұпайлар қосылады
        if self.rect.bottom < SCREEN_HEIGHT // 3:
            COINS += 3
        elif self.rect.bottom < SCREEN_HEIGHT // 1.5:
            COINS += 2
        else:
            COINS += 1
        # Жылдамдықты монеталарды жинаған сайын арттыру
        global c1, c2, c3, c4, c5
        if not c1 and COINS >= 10:
            SPEED += 1
            c1 = True
        if not c2 and COINS >= 20:
            SPEED += 1
            c2 = True
        if not c3 and COINS >= 30:
            SPEED += 1
            c3 = True
        if not c4 and COINS >= 40:
            SPEED += 1
            c4 = True
        if not c5 and COINS >= 50:
            SPEED += 1
            c5 = True
        # Монетаны экраннан қайтадан көрсететін жерге жылжыту
        self.rect.top = random.randint(40, SCREEN_WIDTH - 40)
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))

# Ойыншы (Player) класы
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # Ойыншының қозғалысын басқару
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)

# Спрайттарды орнату
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Спрайт топтарын жасау
enemies = pygame.sprite.Group()
enemies.add(E1)
coinss = pygame.sprite.Group()
coinss.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Жаңа оқиға қосу
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Ойын аяқталған кезде көрсетілетін экран
def game_over_screen():
    screen.fill(RED)
    screen.blit(game_over, (30, 250))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:  # Ойынды жалғастыру үшін SPACE пернесін басу
                    return True
                elif event.key == K_ESCAPE:  # Ойынды тоқтату үшін ESC пернесін басу
                    return False

# Соқтығысуды өңдеу функциясы
def handle_crash():
    time.sleep(2)

background_y = 0  # Фонның y-координатасын бастапқыда орнату

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.1  # Жылдамдықты әр 1 секунд сайын арттыру
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Ойыншы мен қарсылас арасында соқтығысса
    if pygame.sprite.spritecollideany(P1, enemies):
        continue_game = handle_crash()
        if not continue_game:
            pygame.quit()
            sys.exit()

    # Фонды жылжыту
    background_y = (background_y + SPEED) % background.get_height()

    # Фонды экранға орналастыру
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - background.get_height()))

    # Балл мен монеталарды экранға шығару
    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10, 10))

    coins = font_small.render(str(COINS), True, BLACK)
    screen.blit(coins, (370, 10))

    # Барлық спрайттарды жылжыту және қайта салу
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

        # Егер ойыншы монетамен соқтығысса, монеталарды есептеу
        if entity == C1:
            if pygame.sprite.spritecollideany(P1, coinss):
                entity.move()
        else:
            entity.move()

    # Қарсылас машиналарын жылжыту
    for enemy in enemies:
        enemy.move()

    # Монеталарды жылжыту
    for coin in coinss:
        coin.rect.y += SPEED

        # Монеталар экраннан тыс шықса, оларды қайтадан орынға қою
        if coin.rect.top > SCREEN_HEIGHT:
            coin.rect.y = -coin.rect.height
            coin.rect.x = random.randint(40, SCREEN_WIDTH - 40)

    pygame.display.update()
    FramePerSec.tick(FPS)  # FPS-тен басқа жылдамдықты реттеу
