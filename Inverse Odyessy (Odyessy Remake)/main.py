import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Inverse Odyssey")

# Define colors (inverted)
WHITE = (0, 0, 0)
BLACK = (255, 255, 255)
RED = (0, 255, 255)
GREEN = (255, 0, 255)

# Paddle settings
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
PADDLE_SPEED = 5

# Ball settings
BALL_SIZE = 15
ball_speed_x = 4
ball_speed_y = 4

# Initialize paddles and ball
left_paddle = pygame.Rect(30, (HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, (HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)

# Initialize scores
left_score = 0
right_score = 0

# Set up font
font = pygame.font.Font(None, 74)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x = -ball_speed_x

    # Reset ball if it goes out of bounds
    if ball.left <= 0:
        right_score += 1  # Right player scores
        ball.x = WIDTH // 2
        ball.y = HEIGHT // 2
        ball_speed_x = -ball_speed_x
    if ball.right >= WIDTH:
        left_score += 1  # Left player scores
        ball.x = WIDTH // 2
        ball.y = HEIGHT // 2
        ball_speed_x = -ball_speed_x

    # Fill the background with inverted color
    window.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(window, WHITE, left_paddle)
    pygame.draw.rect(window, WHITE, right_paddle)
    pygame.draw.ellipse(window, WHITE, ball)

    # Render scores
    left_score_text = font.render(str(left_score), True, WHITE)
    right_score_text = font.render(str(right_score), True, WHITE)
    window.blit(left_score_text, (WIDTH // 4, 20))
    window.blit(right_score_text, (WIDTH * 3 // 4 - right_score_text.get_width(), 20))

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)