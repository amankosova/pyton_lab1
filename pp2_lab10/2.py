import pygame
import sys
import random
import psycopg2

pygame.init()
CELL_SIZE = 20
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Snake Game")

WHITE = (255, 255, 255)     
CYAN = (0, 255, 255)    
RED = (255, 0, 0)          
PINK = (255, 105, 180)     
BLACK = (0, 0, 0)          
DARK = (47, 79, 79)         

# PostgreSQL дерекқорына қосылу функциясы
def connect():
    return psycopg2.connect(database="lab10", user="postgres", password="270807")

def create():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS user_scores (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE,
                    score INTEGER DEFAULT 0,
                    level INTEGER DEFAULT 1)""")
    conn.commit()
    conn.close()
    cur.close()

def get_user(username):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, score, level FROM user_scores WHERE username = %s", (username,))
    user = cur.fetchone()
    if not user:
        cur.execute("INSERT INTO user_scores (username, score, level) VALUES (%s, 0, 1) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        score = 0
        level = 1
    else:
        user_id, score, level = user
    cur.close()
    conn.close()
    return user_id, score, level

# Ойын барысын сақтау функциясы
def progress(user_id, score, level, state="paused"):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        UPDATE user_scores 
        SET score = %s, level = %s 
        WHERE id = %s
    """, (score, level, user_id))
                
    conn.commit()
    cur.close()
    conn.close()

# Деңгейге жылдамдық
def get_level(level):
    speed = max(5, 10 - level)
    walls = []
    return speed,walls
# Дерекқорды тексеру
create()

# Пайдаланушы логині мен бастапқы мәліметтер
username = input("Логин енгізіңіз: ").strip()
user_id, score, level = get_user(username)
speed, walls = get_level(level)

snake = [[100, 100], [80, 100], [60, 100]]
direction = [CELL_SIZE, 0]
food = [random.randint(1, (700 // CELL_SIZE) - 1) * CELL_SIZE,
        random.randint(1, (500 // CELL_SIZE) - 1) * CELL_SIZE]
paused = False
clock = pygame.time.Clock()

# Қақтығыс тексеру
def collision(pos):
    if pos in snake[1:] or pos[0] < 0 or pos[1] < 0 or pos[0] >= 700 or pos[1] >= 500 or pos in walls:
        return True
    return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            progress(user_id, score, level, "quit")
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
                if paused:
                    progress(user_id, score, level, "paused")
            elif event.key == pygame.K_UP and direction[1] == 0:
                direction = [0, -CELL_SIZE]
            elif event.key == pygame.K_DOWN and direction[1] == 0:
                direction = [0, CELL_SIZE]
            elif event.key == pygame.K_LEFT and direction[0] == 0:
                direction = [-CELL_SIZE, 0]
            elif event.key == pygame.K_RIGHT and direction[0] == 0:
                direction = [CELL_SIZE, 0]

    if not paused:
        new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
        if collision(new_head):
            progress(user_id, score, level, "game over")
            print(f"Game Over! Score: {score}, Level: {level}")
            pygame.quit()
            sys.exit()

        snake.insert(0, new_head)
        if new_head == food:
            score += 1
            if score % 5 == 0:
                level += 1
                speed, walls = get_level(level)
            food = [random.randint(1, (700 // CELL_SIZE) - 1) * CELL_SIZE,
                    random.randint(1, (500 // CELL_SIZE) - 1) * CELL_SIZE]
        else:
            snake.pop()

    # Сурет салу
    screen.fill(BLACK)
    for wall in walls:
        pygame.draw.rect(screen, DARK, (*wall, CELL_SIZE, CELL_SIZE))
    for segment in snake:
        pygame.draw.rect(screen, CYAN, (*segment, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, PINK, (*food, CELL_SIZE, CELL_SIZE))

    font = pygame.font.SysFont("Arial", 20)
    text = font.render(f"{username} = Score: {score} , level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

    if paused:
        pause_text = font.render("ПАУЗА", True, RED)
        screen.blit(pause_text, (700 // 2 - 40, 500 // 2))

    pygame.display.update()
    clock.tick(speed)
