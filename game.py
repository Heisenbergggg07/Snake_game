import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

# ---------------- SETTINGS ----------------
WIDTH, HEIGHT = 600, 400
block_size = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Anaconda Snake 🐍")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

# ---------------- COLORS ----------------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN_HEAD = (0, 200, 0)

# ---------------- LOAD ASSETS ----------------
logo = pygame.image.load("python_logo.png").convert_alpha()
logo = pygame.transform.scale(logo, (block_size * 2, block_size * 2))

# Optional sounds (comment if not using)
try:
    eat_sound = pygame.mixer.Sound("eat.wav")
    gameover_sound = pygame.mixer.Sound("gameover.wav")
except:
    eat_sound = None
    gameover_sound = None

# ---------------- GAME VARIABLES ----------------
high_score = 0


def random_food():
    return (
        random.randint(0, (WIDTH - block_size) // block_size) * block_size,
        random.randint(0, (HEIGHT - block_size) // block_size) * block_size
    )


def draw_grid():
    for x in range(0, WIDTH, block_size):
        for y in range(0, HEIGHT, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen, (30, 30, 30), rect, 1)


def draw_snake(snake):
    for i, (x, y) in enumerate(snake):
        center = (x + block_size // 2, y + block_size // 2)

        if i == 0:
            pygame.draw.circle(screen, GREEN_HEAD, center, block_size // 2 + 3)
            pygame.draw.circle(screen, WHITE, (x + 6, y + 6), 3)
            pygame.draw.circle(screen, BLACK, (x + 6, y + 6), 1)
        else:
            shade = max(100, 255 - i * 3)
            pygame.draw.circle(screen, (0, shade, 0), center, block_size // 2)


def draw_food(food):
    x, y = food
    screen.blit(logo, (x - block_size//2, y - block_size//2))


def show_score(score, high_score):
    text = font.render(f"Score: {score}  High: {high_score}", True, WHITE)
    screen.blit(text, (10, 10))


# ---------------- START SCREEN ----------------
def start_screen():
    while True:
        screen.fill(BLACK)

        title = font.render("ANACONDA SNAKE 🐍", True, WHITE)
        msg = font.render("Press SPACE to Start", True, WHITE)

        screen.blit(title, (WIDTH//2 - 120, HEIGHT//2 - 40))
        screen.blit(msg, (WIDTH//2 - 130, HEIGHT//2))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return


# ---------------- GAME OVER SCREEN ----------------
def game_over_screen(score):
    global high_score

    if score > high_score:
        high_score = score

    while True:
        screen.fill(BLACK)

        over = font.render("GAME OVER", True, WHITE)
        scr = font.render(f"Score: {score}", True, WHITE)
        msg = font.render("Press R to Restart", True, WHITE)

        screen.blit(over, (WIDTH//2 - 80, HEIGHT//2 - 40))
        screen.blit(scr, (WIDTH//2 - 60, HEIGHT//2))
        screen.blit(msg, (WIDTH//2 - 110, HEIGHT//2 + 40))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return


# ---------------- MAIN GAME LOOP ----------------
def game_loop():
    snake = [(100, 100)]
    direction = (block_size, 0)
    food = random_food()
    score = 0

    running = True

    while running:
        speed = 12 + score // 3
        clock.tick(speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, block_size):
                    direction = (0, -block_size)
                elif event.key == pygame.K_DOWN and direction != (0, -block_size):
                    direction = (0, block_size)
                elif event.key == pygame.K_LEFT and direction != (block_size, 0):
                    direction = (-block_size, 0)
                elif event.key == pygame.K_RIGHT and direction != (-block_size, 0):
                    direction = (block_size, 0)

        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, head)

        # Eating food
        if abs(head[0] - food[0]) < block_size and abs(head[1] - food[1]) < block_size:
            score += 1
            food = random_food()
            if eat_sound:
                eat_sound.play()
        else:
            snake.pop()

        # Collision
        if (
            head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT or
            head in snake[1:]
        ):
            if gameover_sound:
                gameover_sound.play()
            game_over_screen(score)
            return

        # Draw everything
        screen.fill(BLACK)
        draw_grid()
        draw_snake(snake)
        draw_food(food)
        show_score(score, high_score)

        pygame.display.update()


# ---------------- RUN GAME ----------------
while True:
    start_screen()
    game_loop()