import pygame
import sys
import random
import Components.score as score
import Components.sounds as sounds
import Components.itemBox as box
import Mods.paddleShrink as paddleShrink

# General setup
pygame.init()
clock = pygame.time.Clock()
pygame.font.init()

# Global variables
ballSpeedX = 7
ballSpeedY = 7
playerSpeed = 10
opponentSpeed = 6

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
    global ballSpeedX, ballSpeedY, playerScore, opponentScore
    pygame.draw.ellipse(screen, lightGrey, ball)
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    # Bounce off top and bottom
    if (ball.top <= 0 or ball.bottom >= screenHeight):
        ballSpeedY *= -1

    # Bounce off left and right
    if (ball.left <= 0):
        sounds.playScoreSound()
        ballRestart()
        score.increase_player_score()

    if (ball.right >= screenWidth):
        sounds.playScoreSound()
        ballRestart()
        score.increase_opponent_score()

    # Bounce off player
    if (ball.colliderect(player)):
        sounds.playPongSound()
        ballSpeedX *= -1
        if (ball.y > player.centery + 20):
            ballSpeedY = abs(ballSpeedY)
        elif (ball.y < player.centery - 20):
            ballSpeedY = -abs(ballSpeedY)

    # Bounce off opponent
    if (ball.colliderect(opponent)):
        sounds.playPongSound()
        ballSpeedX *= -1
        if (ball.y > opponent.centery + 20):
            ballSpeedY = abs(ballSpeedY)
        elif (ball.y < opponent.centery - 20):
            ballSpeedY = -abs(ballSpeedY)

    # Collision with item box
    # TODO: Add modes for the item box
    if ball.colliderect(box.getBox()):
        sounds.playAlienSound()
        box.removeBox()
        if(ballSpeedX < 0):
            opponent.inflate_ip(paddleShrink.shrinkPaddle(opponent.height))
        else:
            player.inflate_ip(paddleShrink.shrinkPaddle(player.height))


def ballRestart():
    global ballSpeedX, ballSpeedY
    ball.x = screenWidth/2-15
    ball.y = screenHeight/2-15
    ballSpeedX *= random.choice((1, -1))
    ballSpeedY *= random.choice((1, -1))


def playerMovement():
    global playerSpeed
    # Controlled with the up and down arrow keys
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            player.y += playerSpeed
            if (player.bottom >= screenHeight):
                player.bottom = screenHeight
        if event.key == pygame.K_UP:
            player.y -= playerSpeed
            if (player.top <= 0):
                player.top = 0
    return

# Opponent follows the ball on the y axis


def opponentMovement():
    global playerSpeed
    if ball.y > opponent.y:
        opponent.y += opponentSpeed
        if (opponent.bottom >= screenHeight):
            opponent.bottom = screenHeight
    if ball.y < opponent.y:
        opponent.y -= opponentSpeed
        if (opponent.top <= 0):
            opponent.top = 0


if __name__ == "__main__":

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
        pygame.draw.rect(screen, lightGrey,
                         box.spawnBox(pygame.time.get_ticks()))
        pygame.draw.rect(screen, lightGrey, player)
        pygame.draw.rect(screen, lightGrey, opponent)

        # Update scores
        score.draw_scores(screen, screenWidth, screenHeight)

        # Move objects
        ballMovement()
        playerMovement()
        opponentMovement()

        # updating the window
        pygame.display.flip()
        clock.tick(60)
