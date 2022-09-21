import pygame
import sys

# General setup
pygame.init()
clock = pygame.time.Clock()

# Global variables
ballSpeedX = 7
ballSpeedY = 7
playerSpeed = 10

# colors
bgColor = pygame.Color('grey12')
lightGrey = (200, 200, 200)

# Setting up main window
screenWidth = 1200
screenHeight = 700
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Pong')

# Game Rectangles
ball = pygame.Rect(screenWidth/2-15, screenHeight/2-15, 30, 30)
player = pygame.Rect(screenWidth-20, screenHeight/2-70, 10, 140)
opponent = pygame.Rect(10, screenHeight/2-70, 10, 140)


def ballMovement():
    global ballSpeedX, ballSpeedY
    pygame.draw.ellipse(screen, lightGrey, ball)
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    # Bounce off top and bottom
    if (ball.top <= 0 or ball.bottom >= screenHeight):
        ballSpeedY *= -1

    # Bounce off left and right
    if (ball.left <= 0 or ball.right >= screenWidth):
        ball.x = screenWidth/2-15
        ball.y = screenHeight/2-15

    # Bounce off player
    if (ball.colliderect(player) or ball.colliderect(opponent)):
        ballSpeedX *= -1


def playerMovement():
    global playerSpeed
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            player.y += playerSpeed
        if event.key == pygame.K_UP:
            player.y -= playerSpeed
    return

def opponentMovement():
    global playerSpeed
    if ball.y > opponent.y:
        opponent.y += playerSpeed - 4
    if ball.y < opponent.y:
        opponent.y -= playerSpeed - 4


# Game loop
while True:
    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw objects
    screen.fill(bgColor)
    pygame.draw.aaline(screen, lightGrey, (screenWidth/2, 0),
                       (screenWidth/2, screenHeight))
    pygame.draw.rect(screen, lightGrey, player)
    pygame.draw.rect(screen, lightGrey, opponent)

    ballMovement()
    playerMovement()
    opponentMovement()

    # updating the window
    pygame.display.flip()
    clock.tick(60)
