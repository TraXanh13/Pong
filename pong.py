import pygame, sys, random

# General setup
pygame.init()
clock = pygame.time.Clock()
pygame.font.init()
pygame.mixer.pre_init(44100, -16, 2, 512)

# Global variables
ballSpeedX = 7
ballSpeedY = 7
playerSpeed = 10
playerScore = 0
opponentScore = 0

# colors
bgColor = pygame.Color('grey12')
lightGrey = (200, 200, 200)

# Sound variables (Supports wav and ogg files)
pongSound = pygame.mixer.Sound('./media/pong.ogg')
scoreSound = pygame.mixer.Sound('./media/score.ogg')

# Setting up main window
screenWidth = 1200
screenHeight = 700
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Pong')

# Scores
font = pygame.font.SysFont("arial", 64)
playerScoreText = font.render(str(playerScore), False, lightGrey)
opponentScoreText = font.render(str(opponentScore), False, lightGrey)

# Game Rectangles
ball = pygame.Rect(screenWidth/2-15, screenHeight/2-15, 30, 30)
player = pygame.Rect(screenWidth-20, screenHeight/2-70, 10, 140)
opponent = pygame.Rect(10, screenHeight/2-70, 10, 140)
playerScoreRect = playerScoreText.get_rect(center=(700, 350))
opponentScoreRect = opponentScoreText.get_rect(center=(500, 350))


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
        pygame.mixer.Sound.play(scoreSound)
        ballRestart()
        playerScore += 1

    if (ball.right >= screenWidth):
        ballRestart()
        opponentScore += 1

    # Bounce off player
    if (ball.colliderect(player) or ball.colliderect(opponent)):
        pygame.mixer.Sound.play(pongSound)
        ballSpeedX *= -1

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
            if(player.bottom >= screenHeight):
                player.bottom = screenHeight
        if event.key == pygame.K_UP:
            player.y -= playerSpeed
            if(player.top <= 0):
                player.top = 0
    return

# Opponent follows the ball on the y axis
def opponentMovement():
    global playerSpeed
    if ball.y > opponent.y:
        opponent.y += playerSpeed - 4
        if(opponent.bottom >= screenHeight):
            opponent.bottom = screenHeight
    if ball.y < opponent.y:
        opponent.y -= playerSpeed - 4
        if(opponent.top <= 0):
            opponent.top = 0

if __name__ == "__main__":
    
    # Game loop
    while True:
        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update scores
        playerScoreText = font.render(str(playerScore), False, lightGrey)
        opponentScoreText = font.render(str(opponentScore), False, lightGrey)

        # Draw objects
        screen.fill(bgColor)
        pygame.draw.aaline(screen, lightGrey, (screenWidth/2, 0),
                        (screenWidth/2, screenHeight))
        pygame.draw.rect(screen, lightGrey, player)
        pygame.draw.rect(screen, lightGrey, opponent)
        screen.blit(playerScoreText, playerScoreRect)
        screen.blit(opponentScoreText, opponentScoreRect)

        # Move objects
        ballMovement()
        playerMovement()
        opponentMovement()

        # updating the window
        pygame.display.flip()
        clock.tick(60)