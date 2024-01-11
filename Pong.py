import pygame
import sys

fps = int(input("enter speed. Default-30: "))
WIDT = int(input("Enter screen width. Default-800: "))
HEIGH = int(input("Enter screen height. Default-600: "))
BALLSPEED = int(input("Enter ball speed. Default-5: "))
PADDLESPEED = int(input("Enter paddle speed. Default-10: "))
red = int(input("Enter red brightness. Min-0, Max-255: "))
green = int(input("Enter green brightness. Min-0, Max-255: "))
blue = int(input("Enter blue brightness. Min-0, Max-255: "))
# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = WIDT, HEIGH
BALL_SPEED = BALLSPEED
PADDLE_SPEED = PADDLESPEED

# Colors
WHITE = (red, green, blue)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Player Pong")

# Create game objects
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_speed_x = BALL_SPEED
ball_speed_y = BALL_SPEED

player1_paddle = pygame.Rect(WIDTH - 50 - 20, HEIGHT // 2 - 50, 20, 100)
player2_paddle = pygame.Rect(30, HEIGHT // 2 - 50, 20, 100)

# Game variables
font = pygame.font.Font(None, 36)
player1_score = 0
player2_score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    player1_paddle.y -= keys[pygame.K_UP] * PADDLE_SPEED
    player1_paddle.y += keys[pygame.K_DOWN] * PADDLE_SPEED

    player2_paddle.y -= keys[pygame.K_w] * PADDLE_SPEED
    player2_paddle.y += keys[pygame.K_s] * PADDLE_SPEED

    # Ensure paddles stay within the valid range
    player1_paddle.y = max(0, min(player1_paddle.y, HEIGHT - player1_paddle.height))
    player2_paddle.y = max(0, min(player2_paddle.y, HEIGHT - player2_paddle.height))

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_speed_x = -ball_speed_x

    # Ball out of bounds
    if ball.left <= 0:
        player2_score += 1
        print("Player 2 Score:", player2_score)
        ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        ball_speed_x = BALL_SPEED
        ball_speed_y = BALL_SPEED
    elif ball.right >= WIDTH:
        player1_score += 1
        print("Player 1 Score:", player1_score)
        ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        ball_speed_x = -BALL_SPEED
        ball_speed_y = BALL_SPEED

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, player1_paddle)
    pygame.draw.rect(screen, WHITE, player2_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Update the display
    pygame.display.flip()

    # Control the game's speed
    pygame.time.delay(fps)
