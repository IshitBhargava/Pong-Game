import pygame
import sys
import random

a = int(input("enter ball speed: "))
b = int(input("enter paddle speed: "))
c = int(input("red brightness: "))
d = int(input("green brightness: "))
e = int(input("blue brightness: "))
f = input("screen title: ")

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = a
PADDLE_SPEED = b

# Colors
WHITE = (c, d, e)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f)

# Create game objects
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_speed_x = BALL_SPEED * random.choice([1, -1])
ball_speed_y = BALL_SPEED * random.choice([1, -1])

player_paddle = pygame.Rect(WIDTH - 50 - 20, HEIGHT // 2 - 50, 20, 100)
computer_paddle = pygame.Rect(30, HEIGHT // 2 - 50, 20, 100)

# Game variables
font = pygame.font.Font(None, 36)
player_score = 0
computer_score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the player paddle
    keys = pygame.key.get_pressed()
    player_paddle.y -= keys[pygame.K_UP] * PADDLE_SPEED
    player_paddle.y += keys[pygame.K_DOWN] * PADDLE_SPEED

    # Ensure player paddle stays within the valid range
    player_paddle.y = max(0, min(player_paddle.y, HEIGHT - player_paddle.height))

    # Move the computer paddle to track the ball
    if ball.centery < computer_paddle.centery:
        computer_paddle.y -= PADDLE_SPEED
    elif ball.centery > computer_paddle.centery:
        computer_paddle.y += PADDLE_SPEED

    # Ensure computer paddle stays within the valid range
    computer_paddle.y = max(0, min(computer_paddle.y, HEIGHT - computer_paddle.height))

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    if ball.colliderect(player_paddle) or ball.colliderect(computer_paddle):
        ball_speed_x = -ball_speed_x

    # Ball out of bounds
    if ball.left <= 0:
        player_score += 1
        print("Player Score:", player_score)
        ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        ball_speed_x = BALL_SPEED * random.choice([1, -1])
        ball_speed_y = BALL_SPEED * random.choice([1, -1])
    elif ball.right >= WIDTH:
        computer_score += 1
        print("Computer Score:", computer_score)
        ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        ball_speed_x = BALL_SPEED * random.choice([1, -1])
        ball_speed_y = BALL_SPEED * random.choice([1, -1])

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, computer_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Update the display
    pygame.display.flip()

    # Control the game's speed
    pygame.time.delay(30)
